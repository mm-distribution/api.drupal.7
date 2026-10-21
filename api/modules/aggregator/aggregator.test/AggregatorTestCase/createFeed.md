# AggregatorTestCase::createFeed()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 33–41 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L33-L41)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function createFeed($feed_url = NULL)
```

## Documentation

```text
Creates an aggregator feed.

This method simulates the form submission on path
admin/config/services/aggregator/add/feed.

@param $feed_url
  (optional) If given, feed will be created with this URL, otherwise
  /rss.xml will be used. Defaults to NULL.

@return $feed
  Full feed object if possible.

@see getFeedEditArray()
```

## Code

```php
  function createFeed($feed_url = NULL) {
    $edit = $this->getFeedEditArray($feed_url);
    $this->drupalPost('admin/config/services/aggregator/add/feed', $edit, t('Save'));
    $this->assertRaw(t('The feed %name has been added.', array('%name' => $edit['title'])), format_string('The feed !name has been added.', array('!name' => $edit['title'])));

    $feed = db_query("SELECT *  FROM {aggregator_feed} WHERE title = :title AND url = :url", array(':title' => $edit['title'], ':url' => $edit['url']))->fetch();
    $this->assertTrue(!empty($feed), 'The feed found in database.');
    return $feed;
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
