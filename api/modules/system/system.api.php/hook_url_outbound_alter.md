# hook_url_outbound_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4353–4367 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4353-L4367)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_url_outbound_alter(&$path, &$options, $original_path)
```

## Documentation

```text
Alters outbound URLs.

@param $path
  The outbound path to alter, not adjusted for path aliases yet. It won't be
  adjusted for path aliases until all modules are finished altering it, thus
  being consistent with hook_url_inbound_alter(), which adjusts for all path
  aliases before allowing modules to alter it. This may have been altered by
  other modules before this one.
@param $options
  A set of URL options for the URL so elements such as a fragment or a query
  string can be added to the URL.
@param $original_path
  The original path, before being altered by any modules.

@see url()
```

## Code

```php
function hook_url_outbound_alter(&$path, &$options, $original_path) {
  // Use an external RSS feed rather than the Drupal one.
  if ($path == 'rss.xml') {
    $path = 'http://example.com/rss.xml';
    $options['external'] = TRUE;
  }

  // Instead of pointing to user/[uid]/edit, point to user/me/edit.
  if (preg_match('|^user/([0-9]*)/edit(/.*)?|', $path, $matches)) {
    global $user;
    if ($user->uid == $matches[1]) {
      $path = 'user/me/edit' . $matches[2];
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_url_outbound_alter()".

- [url_alter_test_url_outbound_alter()](../../simpletest/tests/url_alter_test.module/url_alter_test_url_outbound_alter.md) — `modules/simpletest/tests/url_alter_test.module`
- [locale_url_outbound_alter()](../../locale/locale.module/locale_url_outbound_alter.md) — `modules/locale/locale.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
