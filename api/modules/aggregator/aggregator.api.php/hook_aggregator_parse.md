# hook_aggregator_parse()

- **Type:** Hook (documentation function)
- **File:** [`modules/aggregator/aggregator.api.php`](_file.md), lines 110–116 · [local source](../../../../source/modules/aggregator/aggregator.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.api.php#L110-L116)
- **Module/theme:** aggregator
- **Topics:** [hooks](../../../topics/hooks.md), aggregator

## Signature

```php
function hook_aggregator_parse($feed)
```

## Documentation

```text
Create an alternative parser for aggregator module.

A parser converts feed item data to a common format. The parser is called
at the second of the three aggregation stages: first, data is downloaded
by the active fetcher; second, it is converted to a common format by the
active parser; and finally, it is passed to all active processors which
manipulate or store the data.

Modules that define this hook can be set as the active parser within the
configuration page. Only one parser can be active at a time.

@param $feed
  An object describing the resource to be parsed. $feed->source_string
  contains the raw feed data. The hook implementation should parse this data
  and add the following properties to the $feed object:
  - description: The human-readable description of the feed.
  - link: A full URL that directly relates to the feed.
  - image: An image URL used to display an image of the feed.
  - etag: An entity tag from the HTTP header used for cache validation to
    determine if the content has been changed.
  - modified: The UNIX timestamp when the feed was last modified.
  - items: An array of feed items. The common format for a single feed item
    is an associative array containing:
    - title: The human-readable title of the feed item.
    - description: The full body text of the item or a summary.
    - timestamp: The UNIX timestamp when the feed item was last published.
    - author: The author of the feed item.
    - guid: The global unique identifier (GUID) string that uniquely
      identifies the item. If not available, the link is used to identify
      the item.
    - link: A full URL to the individual feed item.

@return
  TRUE if parsing was successful, FALSE otherwise.

@see hook_aggregator_parse_info()
@see hook_aggregator_fetch()
@see hook_aggregator_process()

@ingroup aggregator
```

## Code

```php
function hook_aggregator_parse($feed) {
  if ($items = mymodule_parse($feed->source_string)) {
    $feed->items = $items;
    return TRUE;
  }
  return FALSE;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_aggregator_parse()".

- [aggregator_aggregator_parse()](../aggregator.parser.inc/aggregator_aggregator_parse.md) — `modules/aggregator/aggregator.parser.inc`

---
_Drupal 7.103 · [modules/aggregator/aggregator.api.php](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
