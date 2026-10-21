# hook_aggregator_fetch_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/aggregator/aggregator.api.php`](_file.md), lines 61–66 · [local source](../../../../source/modules/aggregator/aggregator.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.api.php#L61-L66)
- **Module/theme:** aggregator
- **Topics:** [hooks](../../../topics/hooks.md), aggregator

## Signature

```php
function hook_aggregator_fetch_info()
```

## Documentation

```text
Specify the title and short description of your fetcher.

The title and the description provided are shown within the configuration
page. Use as title the human readable name of the fetcher and as description
a brief (40 to 80 characters) explanation of the fetcher's functionality.

This hook is only called if your module implements hook_aggregator_fetch().
If this hook is not implemented aggregator will use your module's file name
as title and there will be no description.

@return
  An associative array defining a title and a description string.

@see hook_aggregator_fetch()

@ingroup aggregator
```

## Code

```php
function hook_aggregator_fetch_info() {
  return array(
    'title' => t('Default fetcher'),
    'description' => t('Default fetcher for resources available by URL.'),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_aggregator_fetch_info()".

- [aggregator_aggregator_fetch_info()](../aggregator.fetcher.inc/aggregator_aggregator_fetch_info.md) — `modules/aggregator/aggregator.fetcher.inc`

---
_Drupal 7.103 · [modules/aggregator/aggregator.api.php](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
