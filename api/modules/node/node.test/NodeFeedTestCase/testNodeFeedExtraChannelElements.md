# NodeFeedTestCase::testNodeFeedExtraChannelElements()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2034–2040 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2034-L2040)
- **Class:** [NodeFeedTestCase](../NodeFeedTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeFeedExtraChannelElements()
```

## Documentation

```text
Ensures that node_feed() accepts and prints extra channel elements.
```

## Code

```php
  function testNodeFeedExtraChannelElements() {
    ob_start();
    node_feed(array(), array('copyright' => 'Drupal is a registered trademark of Dries Buytaert.'));
    $output = ob_get_clean();

    $this->assertTrue(strpos($output, '<copyright>Drupal is a registered trademark of Dries Buytaert.</copyright>') !== FALSE);
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
