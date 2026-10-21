# hook_aggregator_fetch()

- **Type:** Hook (documentation function)
- **File:** [`modules/aggregator/aggregator.api.php`](_file.md), lines 39–41 · [local source](../../../../source/modules/aggregator/aggregator.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.api.php#L39-L41)
- **Module/theme:** aggregator
- **Topics:** [hooks](../../../topics/hooks.md), aggregator

## Signature

```php
function hook_aggregator_fetch($feed)
```

## Documentation

```text
Create an alternative fetcher for aggregator.module.

A fetcher downloads feed data to a Drupal site. The fetcher is called at the
first of the three aggregation stages: first, data is downloaded by the
active fetcher; second, it is converted to a common format by the active
parser; and finally, it is passed to all active processors, which manipulate
or store the data.

Modules that define this hook can be set as the active fetcher within the
configuration page. Only one fetcher can be active at a time.

@param $feed
  A feed object representing the resource to be downloaded. $feed->url
  contains the link to the feed. Download the data at the URL and expose it
  to other modules by attaching it to $feed->source_string.

@return
  TRUE if fetching was successful, FALSE otherwise.

@see hook_aggregator_fetch_info()
@see hook_aggregator_parse()
@see hook_aggregator_process()

@ingroup aggregator
```

## Code

```php
function hook_aggregator_fetch($feed) {
  $feed->source_string = mymodule_fetch($feed->url);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_aggregator_fetch()".

- [aggregator_aggregator_fetch()](../aggregator.fetcher.inc/aggregator_aggregator_fetch.md) — `modules/aggregator/aggregator.fetcher.inc`

---
_Drupal 7.103 · [modules/aggregator/aggregator.api.php](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
