# system_hook_info()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 261–276 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L261-L276)
- **Module/theme:** system
- **Implements:** [hook_hook_info()](../system.api.php/hook_hook_info.md)

## Signature

```php
function system_hook_info()
```

## Documentation

```text
Implements hook_hook_info().
```

## Code

```php
function system_hook_info() {
  $hooks['token_info'] = array(
    'group' => 'tokens',
  );
  $hooks['token_info_alter'] = array(
    'group' => 'tokens',
  );
  $hooks['tokens'] = array(
    'group' => 'tokens',
  );
  $hooks['tokens_alter'] = array(
    'group' => 'tokens',
  );

  return $hooks;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
