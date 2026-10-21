# filter_xss()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1538–1571 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1538-L1571)
- **Topics:** [sanitization](../../topics/sanitization.md)

## Signature

```php
function filter_xss($string, $allowed_tags = array('a', 'em', 'strong', 'cite', 'blockquote', 'code', 'ul', 'ol', 'li', 'dl', 'dt', 'dd'))
```

## Documentation

```text
Filters HTML to prevent cross-site-scripting (XSS) vulnerabilities.

Based on kses by Ulf Harnhammar, see http://sourceforge.net/projects/kses.
For examples of various XSS attacks, see: http://ha.ckers.org/xss.html.

This code does four things:
- Removes characters and constructs that can trick browsers.
- Makes sure all HTML entities are well-formed.
- Makes sure all HTML tags and attributes are well-formed.
- Makes sure no HTML tags contain URLs with a disallowed protocol (e.g.
  javascript:).

@param $string
  The string with raw HTML in it. It will be stripped of everything that can
  cause an XSS attack.
@param $allowed_tags
  An array of allowed tags.

@return
  An XSS safe version of $string, or an empty string if $string is not
  valid UTF-8.

@see drupal_validate_utf8()
```

## Code

```php
function filter_xss($string, $allowed_tags = array('a', 'em', 'strong', 'cite', 'blockquote', 'code', 'ul', 'ol', 'li', 'dl', 'dt', 'dd')) {
  // Only operate on valid UTF-8 strings. This is necessary to prevent cross
  // site scripting issues on Internet Explorer 6.
  if (!drupal_validate_utf8($string)) {
    return '';
  }
  // Store the text format.
  _filter_xss_split($allowed_tags, TRUE);
  // Remove NULL characters (ignored by some browsers).
  $string = str_replace(chr(0), '', (string) $string);
  // Remove Netscape 4 JS entities.
  $string = preg_replace('%&\s*\{[^}]*(\}\s*;?|$)%', '', $string);

  // Defuse all HTML entities.
  $string = str_replace('&', '&amp;', $string);
  // Change back only well-formed entities in our whitelist:
  // Decimal numeric entities.
  $string = preg_replace('/&amp;#([0-9]+;)/', '&#\1', $string);
  // Hexadecimal numeric entities.
  $string = preg_replace('/&amp;#[Xx]0*((?:[0-9A-Fa-f]{2})+;)/', '&#x\1', $string);
  // Named entities.
  $string = preg_replace('/&amp;([A-Za-z][A-Za-z0-9]*;)/', '&\1', $string);

  return preg_replace_callback('%
    (
    <(?=[^a-zA-Z!/])  # a lone <
    |                 # or
    <!--.*?-->        # a comment
    |                 # or
    <[^>]*(>|$)       # a string that starts with a <, up until the > or the end of the string
    |                 # or
    >                 # just a >
    )%x', '_filter_xss_split', $string);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
