# NodeTitleTestCase::testNodeTitle()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1991–2016 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1991-L2016)
- **Class:** [NodeTitleTestCase](../NodeTitleTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeTitle()
```

## Documentation

```text
 Creates one node and tests if the node title has the correct value.
```

## Code

```php
  function testNodeTitle() {
    // Create "Basic page" content with title.
    // Add the node to the frontpage so we can test if teaser links are clickable.
    $settings = array(
      'title' => $this->randomName(8),
      'promote' => 1,
    );
    $node = $this->drupalCreateNode($settings);

    // Test <title> tag.
    $this->drupalGet("node/$node->nid");
    $xpath = '//title';
    $this->assertEqual(current($this->xpath($xpath)), $node->title .' | Drupal', 'Page title is equal to node title.', 'Node');

    // Test breadcrumb in comment preview.
    $this->drupalGet("comment/reply/$node->nid");
    $xpath = '//div[@class="breadcrumb"]/a[last()]';
    $this->assertEqual(current($this->xpath($xpath)), $node->title, 'Node breadcrumb is equal to node title.', 'Node');

    // Test node title in comment preview.
    $this->assertEqual(current($this->xpath('//div[@id=:id]/h2/a', array(':id' => 'node-' . $node->nid))), $node->title, 'Node preview title is equal to node title.', 'Node');

    // Test node title is clickable on teaser list (/node).
    $this->drupalGet('node');
    $this->clickLink($node->title);
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
