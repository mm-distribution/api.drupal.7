# aggregator_update_7004()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.install`](_file.md), lines 332–336 · [local source](../../../../source/modules/aggregator/aggregator.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.install#L332-L336)
- **Module/theme:** aggregator
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function aggregator_update_7004()
```

## Documentation

```text
Add index on timestamp.
```

## Code

```php
function aggregator_update_7004() {
  if (!db_index_exists('aggregator_item', 'timestamp')) {
    db_add_index('aggregator_item', 'timestamp', array('timestamp'));
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.install](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.install) · Licensed GPL-2.0-or-later (see LICENSE)._
