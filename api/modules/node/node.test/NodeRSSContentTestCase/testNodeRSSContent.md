# NodeRSSContentTestCase::testNodeRSSContent()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 966–999 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L966-L999)
- **Class:** [NodeRSSContentTestCase](../NodeRSSContentTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeRSSContent()
```

## Documentation

```text
Ensures that a new node includes the custom data when added to an RSS feed.
```

## Code

```php
  function testNodeRSSContent() {
    // Create a node.
    $node = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));

    $this->drupalGet('rss.xml');

    // Check that content added in 'rss' view mode appear in RSS feed.
    $rss_only_content = t('Extra data that should appear only in the RSS feed for node !nid.', array('!nid' => $node->nid));
    $this->assertText($rss_only_content, 'Node content designated for RSS appear in RSS feed.');

    // Check that content added in view modes other than 'rss' doesn't
    // appear in RSS feed.
    $non_rss_content = t('Extra data that should appear everywhere except the RSS feed for node !nid.', array('!nid' => $node->nid));
    $this->assertNoText($non_rss_content, 'Node content not designed for RSS doesn\'t appear in RSS feed.');

    // Check that extra RSS elements and namespaces are added to RSS feed.
    $test_element = array(
      'key' => 'testElement',
      'value' => t('Value of testElement RSS element for node !nid.', array('!nid' => $node->nid)),
    );
    $test_ns = 'xmlns:drupaltest="http://example.com/test-namespace"';
    $this->assertRaw(format_xml_elements(array($test_element)), 'Extra RSS elements appear in RSS feed.');
    $this->assertRaw($test_ns, 'Extra namespaces appear in RSS feed.');

    // Check that content added in 'rss' view mode doesn't appear when
    // viewing node.
    $this->drupalGet("node/$node->nid");
    $this->assertNoText($rss_only_content, 'Node content designed for RSS doesn\'t appear when viewing node.');

    // Check that the node feed page does not try to interpret additional path
    // components as arguments for node_feed() and returns default content.
    $this->drupalGet('rss.xml/' . $this->randomName() . '/' . $this->randomName());
    $this->assertText($rss_only_content, 'Ignore page arguments when delivering rss.xml.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
