# _openid_link_href()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 405–413 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L405-L413)
- **Module/theme:** openid

## Signature

```php
function _openid_link_href($rel, $html)
```

## Documentation

```text
Pull the href attribute out of an html link element.
```

## Code

```php
function _openid_link_href($rel, $html) {
  $rel = preg_quote($rel);
  preg_match('|<link\s+rel=["\'](.*)' . $rel . '(.*)["\'](.*)/?>|iUs', $html, $matches);
  if (isset($matches[3])) {
    preg_match('|href=["\']([^"]+)["\']|iU', $matches[3], $href);
    return trim($href[1]);
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
