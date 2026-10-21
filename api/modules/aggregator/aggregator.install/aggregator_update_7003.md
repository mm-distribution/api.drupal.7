# aggregator_update_7003()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.install`](_file.md), lines 320–327 · [local source](../../../../source/modules/aggregator/aggregator.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.install#L320-L327)
- **Module/theme:** aggregator
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function aggregator_update_7003()
```

## Documentation

```text
Increase the length of {aggregator_feed}.url.
```

## Code

```php
function aggregator_update_7003() {
  db_drop_unique_key('aggregator_feed', 'url');
  db_change_field('aggregator_feed', 'url', 'url', array('type' => 'text', 'not null' => TRUE, 'description' => 'URL to the feed.'));
  db_change_field('aggregator_feed', 'link', 'link', array('type' => 'text', 'not null' => TRUE, 'description' => 'The parent website of the feed; comes from the <link> element in the feed.'));
  db_change_field('aggregator_item', 'link', 'link', array('type' => 'text', 'not null' => TRUE, 'description' => 'Link to the feed item.'));
  db_change_field('aggregator_item', 'guid', 'guid', array('type' => 'text', 'not null' => TRUE, 'description' => 'Unique identifier for the feed item.'));
  db_add_index('aggregator_feed', 'url', array(array('url', 255)));
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.install](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.install) · Licensed GPL-2.0-or-later (see LICENSE)._
