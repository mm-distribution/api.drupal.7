# aggregator_update_7001()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.install`](_file.md), lines 291–293 · [local source](../../../../source/modules/aggregator/aggregator.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.install#L291-L293)
- **Module/theme:** aggregator
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function aggregator_update_7001()
```

## Documentation

```text
Add aggregator teaser length to settings from old global default teaser length
```

## Code

```php
function aggregator_update_7001() {
  variable_set('aggregator_teaser_length', variable_get('teaser_length'));
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.install](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.install) · Licensed GPL-2.0-or-later (see LICENSE)._
