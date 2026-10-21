# node_test_node_view()

- **Type:** Function
- **File:** [`modules/node/tests/node_test.module`](_file.md), lines 30–52 · [local source](../../../../../source/modules/node/tests/node_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module#L30-L52)
- **Module/theme:** node_test
- **Implements:** [hook_node_view()](../../node.api.php/hook_node_view.md)

## Signature

```php
function node_test_node_view($node, $view_mode)
```

## Documentation

```text
Implements hook_node_view().
```

## Code

```php
function node_test_node_view($node, $view_mode) {
  if ($view_mode == 'rss') {
    // Add RSS elements and namespaces when building the RSS feed.
    $node->rss_elements[] = array(
      'key' => 'testElement',
      'value' => t('Value of testElement RSS element for node !nid.', array('!nid' => $node->nid)),
    );
    $node->rss_namespaces['xmlns:drupaltest'] = 'http://example.com/test-namespace';

    // Add content that should be displayed only in the RSS feed.
    $node->content['extra_feed_content'] = array(
      '#markup' => '<p>' . t('Extra data that should appear only in the RSS feed for node !nid.', array('!nid' => $node->nid)) . '</p>',
      '#weight' => 10,
    );
  }

  if ($view_mode != 'rss') {
    // Add content that should NOT be displayed in the RSS feed.
    $node->content['extra_non_feed_content'] = array(
      '#markup' => '<p>' . t('Extra data that should appear everywhere except the RSS feed for node !nid.', array('!nid' => $node->nid)) . '</p>',
    );
  }
}
```

---
_Drupal 7.103 · [modules/node/tests/node_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
