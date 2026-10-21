# hook_aggregator_process()

- **Type:** Hook (documentation function)
- **File:** [`modules/aggregator/aggregator.api.php`](_file.md), lines 168–172 · [local source](../../../../source/modules/aggregator/aggregator.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.api.php#L168-L172)
- **Module/theme:** aggregator
- **Topics:** [hooks](../../../topics/hooks.md), aggregator

## Signature

```php
function hook_aggregator_process($feed)
```

## Documentation

```text
Create a processor for aggregator.module.

A processor acts on parsed feed data. Active processors are called at the
third and last of the aggregation stages: first, data is downloaded by the
active fetcher; second, it is converted to a common format by the active
parser; and finally, it is passed to all active processors that manipulate or
store the data.

Modules that define this hook can be activated as a processor within the
configuration page.

@param $feed
  A feed object representing the resource to be processed. $feed->items
  contains an array of feed items downloaded and parsed at the parsing stage.
  See hook_aggregator_parse() for the basic format of a single item in the
  $feed->items array. For the exact format refer to the particular parser in
  use.

@see hook_aggregator_process_info()
@see hook_aggregator_fetch()
@see hook_aggregator_parse()

@ingroup aggregator
```

## Code

```php
function hook_aggregator_process($feed) {
  foreach ($feed->items as $item) {
    mymodule_save($item);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_aggregator_process()".

- [aggregator_aggregator_process()](../aggregator.processor.inc/aggregator_aggregator_process.md) — `modules/aggregator/aggregator.processor.inc`

---
_Drupal 7.103 · [modules/aggregator/aggregator.api.php](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
