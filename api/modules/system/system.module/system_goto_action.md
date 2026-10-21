# system_goto_action()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3393–3395 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3393-L3395)
- **Module/theme:** system
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function system_goto_action($entity, $context)
```

## Documentation

```text
Redirects to a different URL.

@param $entity
  Ignored.
@param array $context
  Array with the following elements:
  - 'url': URL to redirect to. This will be passed through
    token_replace().
  - Other elements will be used as the data for token replacement.

@ingroup actions
```

## Code

```php
function system_goto_action($entity, $context) {
  drupal_goto(token_replace($context['url'], $context));
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
