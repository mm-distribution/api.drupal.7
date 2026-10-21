# _locale_import_read_po()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 723–975 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L723-L975)
- **Topics:** [locale-api-import-export](../../topics/locale-api-import-export.md)

## Signature

```php
function _locale_import_read_po($op, $file, $mode = NULL, $lang = NULL, $group = 'default')
```

## Documentation

```text
Parses Gettext Portable Object file into an array

@param $op
  Storage operation type: db-store or mem-store.
@param $file
  Drupal file object corresponding to the PO file to import.
@param $mode
  Should existing translations be replaced LOCALE_IMPORT_KEEP or
  LOCALE_IMPORT_OVERWRITE.
@param $lang
  Language code.
@param $group
  Text group to import PO file into (eg. 'default' for interface
  translations).
```

## Code

```php
function _locale_import_read_po($op, $file, $mode = NULL, $lang = NULL, $group = 'default') {

  // The file will get closed by PHP on returning from this function.
  $fd = fopen($file->uri, 'rb');
  if (!$fd) {
    _locale_import_message('The translation import failed, because the file %filename could not be read.', $file);
    return FALSE;
  }

  /*
   * The parser context. Can be:
   *  - 'COMMENT' (#)
   *  - 'MSGID' (msgid)
   *  - 'MSGID_PLURAL' (msgid_plural)
   *  - 'MSGCTXT' (msgctxt)
   *  - 'MSGSTR' (msgstr or msgstr[])
   *  - 'MSGSTR_ARR' (msgstr_arg)
   */
  $context = 'COMMENT';

  // Current entry being read.
  $current = array();

  // Current plurality for 'msgstr[]'.
  $plural = 0;

  // Current line.
  $lineno = 0;

  while (!feof($fd)) {
    // Refresh the time limit every 10 parsed rows to ensure there is always
    // enough time to import the data for large PO files.
    if (!($lineno % 10)) {
      drupal_set_time_limit(30);
    }

    // A line should not be longer than 10 * 1024.
    $line = fgets($fd, 10 * 1024);

    if ($lineno == 0) {
      // The first line might come with a UTF-8 BOM, which should be removed.
      $line = str_replace("\xEF\xBB\xBF", '', $line);
    }

    $lineno++;

    // Trim away the linefeed.
    $line = trim(strtr($line, array("\\\n" => "")));

    if (!strncmp('#', $line, 1)) {
      // Lines starting with '#' are comments.

      if ($context == 'COMMENT') {
        // Already in comment token, insert the comment.
        $current['#'][] = substr($line, 1);
      }
      elseif (($context == 'MSGSTR') || ($context == 'MSGSTR_ARR')) {
        // We are currently in string token, close it out.
        _locale_import_one_string($op, $current, $mode, $lang, $file, $group);

        // Start a new entry for the comment.
        $current         = array();
        $current['#'][]  = substr($line, 1);

        $context = 'COMMENT';
      }
      else {
        // A comment following any other token is a syntax error.
        _locale_import_message('The translation file %filename contains an error: "msgstr" was expected but not found on line %line.', $file, $lineno);
        return FALSE;
      }
    }
    elseif (!strncmp('msgid_plural', $line, 12)) {
      // A plural form for the current message.

      if ($context != 'MSGID') {
        // A plural form cannot be added to anything else but the id directly.
        _locale_import_message('The translation file %filename contains an error: "msgid_plural" was expected but not found on line %line.', $file, $lineno);
        return FALSE;
      }

      // Remove 'msgid_plural' and trim away whitespace.
      $line = trim(substr($line, 12));
      // At this point, $line should now contain only the plural form.

      $quoted = _locale_import_parse_quoted($line);
      if ($quoted === FALSE) {
        // The plural form must be wrapped in quotes.
        _locale_import_message('The translation file %filename contains a syntax error on line %line.', $file, $lineno);
        return FALSE;
      }

      // Append the plural form to the current entry.
      $current['msgid'] .= "\0" . $quoted;

      $context = 'MSGID_PLURAL';
    }
    elseif (!strncmp('msgid', $line, 5)) {
      // Starting a new message.

      if (($context == 'MSGSTR') || ($context == 'MSGSTR_ARR')) {
        // We are currently in a message string, close it out.
        _locale_import_one_string($op, $current, $mode, $lang, $file, $group);

        // Start a new context for the id.
        $current = array();
      }
      elseif ($context == 'MSGID') {
        // We are currently already in the context, meaning we passed an id with no data.
        _locale_import_message('The translation file %filename contains an error: "msgid" is unexpected on line %line.', $file, $lineno);
        return FALSE;
      }

      // Remove 'msgid' and trim away whitespace.
      $line = trim(substr($line, 5));
      // At this point, $line should now contain only the message id.

      $quoted = _locale_import_parse_quoted($line);
      if ($quoted === FALSE) {
        // The message id must be wrapped in quotes.
        _locale_import_message('The translation file %filename contains a syntax error on line %line.', $file, $lineno);
        return FALSE;
      }

      $current['msgid'] = $quoted;
      $context = 'MSGID';
    }
    elseif (!strncmp('msgctxt', $line, 7)) {
      // Starting a new context.

      if (($context == 'MSGSTR') || ($context == 'MSGSTR_ARR')) {
        // We are currently in a message, start a new one.
        _locale_import_one_string($op, $current, $mode, $lang, $file, $group);
        $current = array();
      }
      elseif (!empty($current['msgctxt'])) {
        // A context cannot apply to another context.
        _locale_import_message('The translation file %filename contains an error: "msgctxt" is unexpected on line %line.', $file, $lineno);
        return FALSE;
      }

      // Remove 'msgctxt' and trim away whitespaces.
      $line = trim(substr($line, 7));
      // At this point, $line should now contain the context.

      $quoted = _locale_import_parse_quoted($line);
      if ($quoted === FALSE) {
        // The context string must be quoted.
        _locale_import_message('The translation file %filename contains a syntax error on line %line.', $file, $lineno);
        return FALSE;
      }

      $current['msgctxt'] = $quoted;

      $context = 'MSGCTXT';
    }
    elseif (!strncmp('msgstr[', $line, 7)) {
      // A message string for a specific plurality.

      if (($context != 'MSGID') && ($context != 'MSGCTXT') && ($context != 'MSGID_PLURAL') && ($context != 'MSGSTR_ARR')) {
        // Message strings must come after msgid, msgxtxt, msgid_plural, or other msgstr[] entries.
        _locale_import_message('The translation file %filename contains an error: "msgstr[]" is unexpected on line %line.', $file, $lineno);
        return FALSE;
      }

      // Ensure the plurality is terminated.
      if (strpos($line, ']') === FALSE) {
        _locale_import_message('The translation file %filename contains a syntax error on line %line.', $file, $lineno);
        return FALSE;
      }

      // Extract the plurality.
      $frombracket = strstr($line, '[');
      $plural = substr($frombracket, 1, strpos($frombracket, ']') - 1);

      // Skip to the next whitespace and trim away any further whitespace, bringing $line to the message data.
      $line = trim(strstr($line, " "));

      $quoted = _locale_import_parse_quoted($line);
      if ($quoted === FALSE) {
        // The string must be quoted.
        _locale_import_message('The translation file %filename contains a syntax error on line %line.', $file, $lineno);
        return FALSE;
      }

      $current['msgstr'][$plural] = $quoted;

      $context = 'MSGSTR_ARR';
    }
    elseif (!strncmp("msgstr", $line, 6)) {
      // A string for the an id or context.

      if (($context != 'MSGID') && ($context != 'MSGCTXT')) {
        // Strings are only valid within an id or context scope.
        _locale_import_message('The translation file %filename contains an error: "msgstr" is unexpected on line %line.', $file, $lineno);
        return FALSE;
      }

      // Remove 'msgstr' and trim away away whitespaces.
      $line = trim(substr($line, 6));
      // At this point, $line should now contain the message.

      $quoted = _locale_import_parse_quoted($line);
      if ($quoted === FALSE) {
        // The string must be quoted.
        _locale_import_message('The translation file %filename contains a syntax error on line %line.', $file, $lineno);
        return FALSE;
      }

      $current['msgstr'] = $quoted;

      $context = 'MSGSTR';
    }
    elseif ($line != '') {
      // Anything that is not a token may be a continuation of a previous token.

      $quoted = _locale_import_parse_quoted($line);
      if ($quoted === FALSE) {
        // The string must be quoted.
        _locale_import_message('The translation file %filename contains a syntax error on line %line.', $file, $lineno);
        return FALSE;
      }

      // Append the string to the current context.
      if (($context == 'MSGID') || ($context == 'MSGID_PLURAL')) {
        $current['msgid'] .= $quoted;
      }
      elseif ($context == 'MSGCTXT') {
        $current['msgctxt'] .= $quoted;
      }
      elseif ($context == 'MSGSTR') {
        $current['msgstr'] .= $quoted;
      }
      elseif ($context == 'MSGSTR_ARR') {
        $current['msgstr'][$plural] .= $quoted;
      }
      else {
        // No valid context to append to.
        _locale_import_message('The translation file %filename contains an error: there is an unexpected string on line %line.', $file, $lineno);
        return FALSE;
      }
    }
  }

  // End of PO file, closed out the last entry.
  if (($context == 'MSGSTR') || ($context == 'MSGSTR_ARR')) {
    _locale_import_one_string($op, $current, $mode, $lang, $file, $group);
  }
  elseif ($context != 'COMMENT') {
    _locale_import_message('The translation file %filename ended unexpectedly at line %line.', $file, $lineno);
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
