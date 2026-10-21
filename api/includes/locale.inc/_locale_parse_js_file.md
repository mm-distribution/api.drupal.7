# _locale_parse_js_file()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 1519–1633 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L1519-L1633)

## Signature

```php
function _locale_parse_js_file($filepath)
```

## Documentation

```text
Parses a JavaScript file, extracts strings wrapped in Drupal.t() and
Drupal.formatPlural() and inserts them into the database.
```

## Code

```php
function _locale_parse_js_file($filepath) {
  global $language;

  // The file path might contain a query string, so make sure we only use the
  // actual file.
  $parsed_url = drupal_parse_url($filepath);
  $filepath = $parsed_url['path'];
  // Load the JavaScript file.
  $file = file_get_contents($filepath);

  // Match all calls to Drupal.t() in an array.
  // Note: \s also matches newlines with the 's' modifier.
  preg_match_all('~
    [^\w]Drupal\s*\.\s*t\s*                       # match "Drupal.t" with whitespace
    \(\s*                                         # match "(" argument list start
    (' . LOCALE_JS_STRING . ')\s*                 # capture string argument
    (?:,\s*' . LOCALE_JS_OBJECT . '\s*            # optionally capture str args
      (?:,\s*' . LOCALE_JS_OBJECT_CONTEXT . '\s*) # optionally capture context
    ?)?                                           # close optional args
    [,\)]                                         # match ")" or "," to finish
    ~sx', $file, $t_matches);

  // Match all Drupal.formatPlural() calls in another array.
  preg_match_all('~
    [^\w]Drupal\s*\.\s*formatPlural\s*  # match "Drupal.formatPlural" with whitespace
    \(                                  # match "(" argument list start
    \s*.+?\s*,\s*                       # match count argument
    (' . LOCALE_JS_STRING . ')\s*,\s*   # match singular string argument
    (                             # capture plural string argument
      (?:                         # non-capturing group to repeat string pieces
        (?:
          \'                      # match start of single-quoted string
          (?:\\\\\'|[^\'])*       # match any character except unescaped single-quote
          @count                  # match "@count"
          (?:\\\\\'|[^\'])*       # match any character except unescaped single-quote
          \'                      # match end of single-quoted string
          |
          "                       # match start of double-quoted string
          (?:\\\\"|[^"])*         # match any character except unescaped double-quote
          @count                  # match "@count"
          (?:\\\\"|[^"])*         # match any character except unescaped double-quote
          "                       # match end of double-quoted string
        )
        (?:\s*\+\s*)?             # match "+" with possible whitespace, for str concat
      )+                          # match multiple because we supports concatenating strs
    )\s*                          # end capturing of plural string argument
    (?:,\s*' . LOCALE_JS_OBJECT . '\s*          # optionally capture string args
      (?:,\s*' . LOCALE_JS_OBJECT_CONTEXT . '\s*)?  # optionally capture context
    )?
    [,\)]
    ~sx', $file, $plural_matches);

  $matches = array();

  // Add strings from Drupal.t().
  foreach ($t_matches[1] as $key => $string) {
    $matches[] = array(
      'string'  => $string,
      'context' => $t_matches[2][$key],
    );
  }

  // Add string from Drupal.formatPlural().
  foreach ($plural_matches[1] as $key => $string) {
    $matches[] = array(
      'string'  => $string,
      'context' => $plural_matches[3][$key],
    );

    // If there is also a plural version of this string, add it to the strings array.
    if (isset($plural_matches[2][$key])) {
      $matches[] = array(
        'string'  => $plural_matches[2][$key],
        'context' => $plural_matches[3][$key],
      );
    }
  }

  foreach ($matches as $key => $match) {
    // Remove the quotes and string concatenations from the string.
    $string = implode('', preg_split('~(?<!\\\\)[\'"]\s*\+\s*[\'"]~s', substr($match['string'], 1, -1)));
    $context = implode('', preg_split('~(?<!\\\\)[\'"]\s*\+\s*[\'"]~s', substr($match['context'], 1, -1)));

    $source = db_query("SELECT lid, location FROM {locales_source} WHERE source = :source AND context = :context AND textgroup = 'default'", array(':source' => $string, ':context' => $context))->fetchObject();
    if ($source) {
      // We already have this source string and now have to add the location
      // to the location column, if this file is not yet present in there.
      $locations = preg_split('~\s*;\s*~', (string) $source->location);

      if (!in_array($filepath, $locations)) {
        $locations[] = $filepath;
        $locations = implode('; ', $locations);

        // Save the new locations string to the database.
        db_update('locales_source')
          ->fields(array(
            'location' => $locations,
          ))
          ->condition('lid', $source->lid)
          ->execute();
      }
    }
    else {
      // We don't have the source string yet, thus we insert it into the database.
      db_insert('locales_source')
        ->fields(array(
          'location' => $filepath,
          'source' => $string,
          'context' => $context,
          'textgroup' => 'default',
        ))
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
