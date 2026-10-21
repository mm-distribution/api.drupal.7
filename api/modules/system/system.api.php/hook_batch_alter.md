# hook_batch_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4646–4657 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4646-L4657)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md), [batch](../../../topics/batch.md)

## Signature

```php
function hook_batch_alter(&$batch)
```

## Documentation

```text
Alter batch information before a batch is processed.

Called by batch_process() to allow modules to alter a batch before it is
processed.

@param $batch
  The associative array of batch information. See batch_set() for details on
  what this could contain.

@see batch_set()
@see batch_process()

@ingroup batch
```

## Code

```php
function hook_batch_alter(&$batch) {
  // If the current page request is inside the overlay, add ?render=overlay to
  // the success callback URL, so that it appears correctly within the overlay.
  if (overlay_get_mode() == 'child') {
    if (isset($batch['url_options']['query'])) {
      $batch['url_options']['query']['render'] = 'overlay';
    }
    else {
      $batch['url_options']['query'] = array('render' => 'overlay');
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_batch_alter()".

- [overlay_batch_alter()](../../overlay/overlay.module/overlay_batch_alter.md) — `modules/overlay/overlay.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
