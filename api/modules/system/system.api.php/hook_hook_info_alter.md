# hook_hook_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 55–60 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L55-L60)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_hook_info_alter(&$hooks)
```

## Documentation

```text
Alter information from hook_hook_info().

@param $hooks
  Information gathered by module_hook_info() from other modules'
  implementations of hook_hook_info(). Alter this array directly.
  See hook_hook_info() for information on what this may contain.
```

## Code

```php
function hook_hook_info_alter(&$hooks) {
  // Our module wants to completely override the core tokens, so make
  // sure the core token hooks are not found.
  $hooks['token_info']['group'] = 'mytokens';
  $hooks['tokens']['group'] = 'mytokens';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_hook_info_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
