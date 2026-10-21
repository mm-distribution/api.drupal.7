# hook_trigger_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/trigger/trigger.api.php`](_file.md), lines 72–74 · [local source](../../../../source/modules/trigger/trigger.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.api.php#L72-L74)
- **Module/theme:** trigger
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_trigger_info_alter(&$triggers)
```

## Documentation

```text
Alter triggers declared by hook_trigger_info().

@param $triggers
  Array of trigger information returned by hook_trigger_info()
  implementations. Modify this array in place. See hook_trigger_info()
  for information on what this might contain.
```

## Code

```php
function hook_trigger_info_alter(&$triggers) {
  $triggers['node']['node_insert']['label'] = t('When content is saved');
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_trigger_info_alter()".

_None found._

---
_Drupal 7.103 · [modules/trigger/trigger.api.php](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
