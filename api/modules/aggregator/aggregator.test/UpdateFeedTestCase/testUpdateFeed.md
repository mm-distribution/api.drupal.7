# UpdateFeedTestCase::testUpdateFeed()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 497–524 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L497-L524)
- **Class:** [UpdateFeedTestCase](../UpdateFeedTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function testUpdateFeed()
```

## Documentation

```text
Creates a feed and attempts to update it.
```

## Code

```php
  function testUpdateFeed() {
    $remamining_fields = array('title', 'url', '');
    foreach ($remamining_fields as $same_field) {
      $feed = $this->createFeed();

      // Get new feed data array and modify newly created feed.
      $edit = $this->getFeedEditArray();
      $edit['refresh'] =  1800; // Change refresh value.
      if (isset($feed->{$same_field})) {
        $edit[$same_field] = $feed->{$same_field};
      }
      $this->drupalPost('admin/config/services/aggregator/edit/feed/' . $feed->fid, $edit, t('Save'));
      $this->assertRaw(t('The feed %name has been updated.', array('%name' => $edit['title'])), format_string('The feed %name has been updated.', array('%name' => $edit['title'])));

      // Check feed data.
      $this->assertEqual($this->getUrl(), url('admin/config/services/aggregator/', array('absolute' => TRUE)));
      $this->assertTrue($this->uniqueFeed($edit['title'], $edit['url']), 'The feed is unique.');

      // Check feed source.
      $this->drupalGet('aggregator/sources/' . $feed->fid);
      $this->assertResponse(200, 'Feed source exists.');
      $this->assertText($edit['title'], 'Page title');

      // Delete feed.
      $feed->title = $edit['title']; // Set correct title so deleteFeed() will work.
      $this->deleteFeed($feed);
    }
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
