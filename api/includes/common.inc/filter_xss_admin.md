# filter_xss_admin()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1509–1511 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1509-L1511)
- **Topics:** [sanitization](../../topics/sanitization.md)

## Signature

```php
function filter_xss_admin($string)
```

## Documentation

```text
Applies a very permissive XSS/HTML filter for admin-only use.

Use only for fields where it is impractical to use the
whole filter system, but where some (mainly inline) mark-up
is desired (so check_plain() is not acceptable).

Allows all tags that can be used inside an HTML body, save
for scripts and styles.
```

## Code

```php
function filter_xss_admin($string) {
  return filter_xss($string, array('a', 'abbr', 'acronym', 'address', 'article', 'aside', 'b', 'bdi', 'bdo', 'big', 'blockquote', 'br', 'caption', 'cite', 'code', 'col', 'colgroup', 'command', 'dd', 'del', 'details', 'dfn', 'div', 'dl', 'dt', 'em', 'figcaption', 'figure', 'footer', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hgroup', 'hr', 'i', 'img', 'ins', 'kbd', 'li', 'mark', 'menu', 'meter', 'nav', 'ol', 'output', 'p', 'pre', 'progress', 'q', 'rp', 'rt', 'ruby', 's', 'samp', 'section', 'small', 'span', 'strong', 'sub', 'summary', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th', 'thead', 'time', 'tr', 'tt', 'u', 'ul', 'var', 'wbr'));
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
