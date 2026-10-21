# NodeBuildContent::testNodeRebuildContent()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2232–2241 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2232-L2241)
- **Class:** [NodeBuildContent](../NodeBuildContent.md)
- **Module/theme:** node

## Signature

```php
function testNodeRebuildContent()
```

## Documentation

```text
Ensures that content array is rebuilt on every call to node_build_content().
```

## Code

```php
  function testNodeRebuildContent() {
    $node = $this->drupalCreateNode();

    // Set a property in the content array so we can test for its existence later on.
    $node->content['test_content_property'] = array('#value' => $this->randomString());
    $content = node_build_content($node);

    // If the property doesn't exist it means the node->content was rebuilt.
    $this->assertFalse(isset($content['test_content_property']), 'Node content was emptied prior to being built.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
