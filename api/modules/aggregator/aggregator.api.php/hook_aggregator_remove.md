# hook_aggregator_remove()

- **Type:** Hook (documentation function)
- **File:** [`modules/aggregator/aggregator.api.php`](_file.md), lines 214–216 · [local source](../../../../source/modules/aggregator/aggregator.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.api.php#L214-L216)
- **Module/theme:** aggregator
- **Topics:** [hooks](../../../topics/hooks.md), aggregator

## Signature

```php
function hook_aggregator_remove($feed)
```

## Documentation

```text
Remove stored feed data.

Aggregator calls this hook if either a feed is deleted or a user clicks on
"remove items".

If your module stores feed items for example on hook_aggregator_process() it
is recommended to implement this hook and to remove data related to $feed
when called.

@param $feed
  The $feed object whose items are being removed.

@ingroup aggregator
```

## Code

```php
function hook_aggregator_remove($feed) {
  mymodule_remove_items($feed->fid);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_aggregator_remove()".

- [aggregator_aggregator_remove()](../aggregator.processor.inc/aggregator_aggregator_remove.md) — `modules/aggregator/aggregator.processor.inc`

---
_Drupal 7.103 · [modules/aggregator/aggregator.api.php](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
