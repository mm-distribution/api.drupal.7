# locale_string_is_safe()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 545–563 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L545-L563)

## Signature

```php
function locale_string_is_safe($string)
```

## Documentation

```text
Check that a string is safe to be added or imported as a translation.

This test can be used to detect possibly bad translation strings. It should
not have any false positives. But it is only a test, not a transformation,
as it destroys valid HTML. We cannot reliably filter translation strings
on import because some strings are irreversibly corrupted. For example,
a &amp; in the translation would get encoded to &amp;amp; by filter_xss()
before being put in the database, and thus would be displayed incorrectly.

The allowed tag list is like filter_xss_admin(), but omitting div and img as
not needed for translation and likely to cause layout issues (div) or a
possible attack vector (img).
```

## Code

```php
function locale_string_is_safe($string) {
  // Some strings have tokens in them. For tokens in the first part of href or
  // src HTML attributes, filter_xss() removes part of the token, the part
  // before the first colon.  filter_xss() assumes it could be an attempt to
  // inject javascript. When filter_xss() removes part of tokens, it causes the
  // string to not be translatable when it should be translatable. See
  // LocaleStringIsSafeTest::testLocaleStringIsSafe().
  //
  // We can recognize tokens since they are wrapped with brackets and are only
  // composed of alphanumeric characters, colon, underscore, and dashes. We can
  // be sure these strings are safe to strip out before the string is checked in
  // filter_xss() because no dangerous javascript will match that pattern.
  //
  // @todo Do not strip out the token. Fix filter_xss() to not incorrectly
  //   alter the string. https://www.drupal.org/node/2372127
  $string = preg_replace('/\[[a-z0-9_-]+(:[a-z0-9_-]+)+\]/i', '', $string);

  return decode_entities($string) == decode_entities(filter_xss($string, array('a', 'abbr', 'acronym', 'address', 'b', 'bdo', 'big', 'blockquote', 'br', 'caption', 'cite', 'code', 'col', 'colgroup', 'dd', 'del', 'dfn', 'dl', 'dt', 'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'ins', 'kbd', 'li', 'ol', 'p', 'pre', 'q', 'samp', 'small', 'span', 'strong', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th', 'thead', 'tr', 'tt', 'ul', 'var')));
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
