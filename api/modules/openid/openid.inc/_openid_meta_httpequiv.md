# _openid_meta_httpequiv()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 418–427 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L418-L427)
- **Module/theme:** openid

## Signature

```php
function _openid_meta_httpequiv($equiv, $html)
```

## Documentation

```text
Pull the http-equiv attribute out of an html meta element
```

## Code

```php
function _openid_meta_httpequiv($equiv, $html) {
  preg_match('|<meta\s+http-equiv=["\']' . $equiv . '["\'](.*)/?>|iUs', $html, $matches);
  if (isset($matches[1])) {
    preg_match('|content=["\']([^"]+)["\']|iUs', $matches[1], $content);
    if (isset($content[1])) {
      return $content[1];
    }
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
