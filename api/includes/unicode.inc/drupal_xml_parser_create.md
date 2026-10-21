# drupal_xml_parser_create()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 189–222 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L189-L222)
- **Topics:** [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_xml_parser_create(&$data)
```

## Documentation

```text
Prepares a new XML parser.

This is a wrapper around xml_parser_create() which extracts the encoding
from the XML data first and sets the output encoding to UTF-8. This function
should be used instead of xml_parser_create(), because PHP 4's XML parser
doesn't check the input encoding itself. "Starting from PHP 5, the input
encoding is automatically detected, so that the encoding parameter specifies
only the output encoding."

This is also where unsupported encodings will be converted. Callers should
take this into account: $data might have been changed after the call.

@param $data
  The XML data which will be parsed later.

@return
  An XML parser object or FALSE on error.

@ingroup php_wrappers
```

## Code

```php
function drupal_xml_parser_create(&$data) {
  // Default XML encoding is UTF-8
  $encoding = 'utf-8';
  $bom = FALSE;

  // Check for UTF-8 byte order mark (PHP5's XML parser doesn't handle it).
  if (!strncmp($data, "\xEF\xBB\xBF", 3)) {
    $bom = TRUE;
    $data = substr($data, 3);
  }

  // Check for an encoding declaration in the XML prolog if no BOM was found.
  if (!$bom && preg_match('/^<\?xml[^>]+encoding="(.+?)"/', $data, $match)) {
    $encoding = $match[1];
  }

  // Unsupported encodings are converted here into UTF-8.
  $php_supported = array('utf-8', 'iso-8859-1', 'us-ascii');
  if (!in_array(strtolower($encoding), $php_supported)) {
    $out = drupal_convert_to_utf8($data, $encoding);
    if ($out !== FALSE) {
      $encoding = 'utf-8';
      $data = preg_replace('/^(<\?xml[^>]+encoding)="(.+?)"/', '\\1="utf-8"', $out);
    }
    else {
      watchdog('php', 'Could not convert XML encoding %s to UTF-8.', array('%s' => $encoding), WATCHDOG_WARNING);
      return FALSE;
    }
  }

  $xml_parser = xml_parser_create($encoding);
  xml_parser_set_option($xml_parser, XML_OPTION_TARGET_ENCODING, 'utf-8');
  return $xml_parser;
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
