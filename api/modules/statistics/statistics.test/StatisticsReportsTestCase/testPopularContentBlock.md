# StatisticsReportsTestCase::testPopularContentBlock()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 230–255 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L230-L255)
- **Class:** [StatisticsReportsTestCase](../StatisticsReportsTestCase.md)
- **Module/theme:** statistics

## Signature

```php
function testPopularContentBlock()
```

## Documentation

```text
Tests the "popular content" block.
```

## Code

```php
  function testPopularContentBlock() {
    // Visit a node to have something show up in the block.
    $node = $this->drupalCreateNode(array('type' => 'page', 'uid' => $this->blocking_user->uid));
    $this->drupalGet('node/' . $node->nid);

    // Configure and save the block.
    $block = block_load('statistics', 'popular');
    $block->theme = variable_get('theme_default', 'bartik');
    $block->status = 1;
    $block->pages = '';
    $block->region = 'sidebar_first';
    $block->cache = -1;
    $block->visibility = 0;
    $edit = array('statistics_block_top_day_num' => 3, 'statistics_block_top_all_num' => 3, 'statistics_block_top_last_num' => 3);
    module_invoke('statistics', 'block_save', 'popular', $edit);
    drupal_write_record('block', $block);

    // Get some page and check if the block is displayed.
    $this->drupalGet('user');
    $this->assertText('Popular content', 'Found the popular content block.');
    $this->assertText("Today's", 'Found today\'s popular content.');
    $this->assertText('All time', 'Found the alll time popular content.');
    $this->assertText('Last viewed', 'Found the last viewed popular content.');

    $this->assertRaw(l($node->title, 'node/' . $node->nid), 'Found link to visited node.');
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
