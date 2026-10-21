# drupal_wrap_mail()

- **Type:** Function
- **File:** [`includes/mail.inc`](_file.md), lines 362–390 · [local source](../../../source/includes/mail.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc#L362-L390)

## Signature

```php
function drupal_wrap_mail($text, $indent = '')
```

## Documentation

```text
Performs format=flowed soft wrapping for mail (RFC 3676).

We use delsp=yes wrapping, but only break non-spaced languages when
absolutely necessary to avoid compatibility issues.

We deliberately use LF rather than CRLF, see drupal_mail().

@param string $text
  The plain text to process.
@param string $indent (optional)
  A string to indent the text with. Only '>' characters are repeated on
  subsequent wrapped lines. Others are replaced by spaces.

@return string
  The content of the email as a string with formatting applied.
```

## Code

```php
function drupal_wrap_mail($text, $indent = '') {
  // Convert CRLF into LF.
  $text = str_replace("\r", '', $text);
  // See if soft-wrapping is allowed.
  $clean_indent = _drupal_html_to_text_clean($indent);
  $soft = strpos($clean_indent, ' ') === FALSE;
  // Check if the string has line breaks.
  if (strpos($text, "\n") !== FALSE) {
    // Remove trailing spaces to make existing breaks hard, but leave signature
    // marker untouched (RFC 3676, Section 4.3).
    $text = preg_replace('/(?(?<!^--) +\n|  +\n)/m', "\n", $text);
    // Wrap each line at the needed width.
    $lines = explode("\n", $text);
    array_walk($lines, '_drupal_wrap_mail_line', array('soft' => $soft, 'length' => strlen($indent)));
    $text = implode("\n", $lines);
  }
  else {
    // Wrap this line.
    _drupal_wrap_mail_line($text, 0, array('soft' => $soft, 'length' => strlen($indent)));
  }
  // Empty lines with nothing but spaces.
  $text = preg_replace('/^ +\n/m', "\n", $text);
  // Space-stuff special lines.
  $text = preg_replace('/^(>| |From)/m', ' $1', $text);
  // Apply indentation. We only include non-'>' indentation on the first line.
  $text = $indent . substr(preg_replace('/^/m', $clean_indent, $text), strlen($indent));

  return $text;
}
```

---
_Drupal 7.103 · [includes/mail.inc](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
