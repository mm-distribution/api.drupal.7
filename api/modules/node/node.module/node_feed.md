# node_feed()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2575–2643 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2575-L2643)
- **Module/theme:** node

## Signature

```php
function node_feed($nids = FALSE, $channel = array())
```

## Documentation

```text
Generates and prints an RSS feed.

Generates an RSS feed from an array of node IDs, and prints it with an HTTP
header, with Content Type set to RSS/XML.

@param $nids
  An array of node IDs (nid). Defaults to FALSE so empty feeds can be
  generated with passing an empty array, if no items are to be added
  to the feed.
@param $channel
  An associative array containing title, link, description and other keys,
  to be parsed by format_rss_channel() and format_xml_elements().
  A list of channel elements can be found at the
  @link http://cyber.law.harvard.edu/rss/rss.html RSS 2.0 Specification. @endlink
  The link should be an absolute URL.
```

## Code

```php
function node_feed($nids = FALSE, $channel = array()) {
  global $base_url, $language_content;

  if ($nids === FALSE) {
    $nids = db_select('node', 'n')
      ->fields('n', array('nid', 'created'))
      ->condition('n.promote', 1)
      ->condition('n.status', 1)
      ->orderBy('n.created', 'DESC')
      ->range(0, variable_get('feed_default_items', 10))
      ->addTag('node_access')
      ->execute()
      ->fetchCol();
  }

  $item_length = variable_get('feed_item_length', 'fulltext');
  $namespaces = array('xmlns:dc' => 'http://purl.org/dc/elements/1.1/');

  // Load all nodes to be rendered.
  $nodes = node_load_multiple($nids);
  $items = '';
  foreach ($nodes as $node) {
    $item_text = '';

    $node->link = url("node/$node->nid", array('absolute' => TRUE));
    $node->rss_namespaces = array();
    $account = user_load($node->uid);
    $node->rss_elements = array(
      array('key' => 'pubDate', 'value' => gmdate('r', $node->created)),
      array('key' => 'dc:creator', 'value' => format_username($account)),
      array('key' => 'guid', 'value' => $node->nid . ' at ' . $base_url, 'attributes' => array('isPermaLink' => 'false'))
    );

    // The node gets built and modules add to or modify $node->rss_elements
    // and $node->rss_namespaces.
    $build = node_view($node, 'rss');
    unset($build['#theme']);

    if (!empty($node->rss_namespaces)) {
      $namespaces = array_merge($namespaces, $node->rss_namespaces);
    }

    if ($item_length != 'title') {
      // We render node contents and force links to be last.
      $build['links']['#weight'] = 1000;
      $item_text .= drupal_render($build);
    }

    $items .= format_rss_item($node->title, $node->link, $item_text, $node->rss_elements);
  }

  $channel_defaults = array(
    'version'     => '2.0',
    'title'       => variable_get('site_name', 'Drupal'),
    'link'        => $base_url,
    'description' => variable_get('feed_description', ''),
    'language'    => $language_content->language
  );
  $channel_extras = array_diff_key($channel, $channel_defaults);
  $channel = array_merge($channel_defaults, $channel);

  $output = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n";
  $output .= "<rss version=\"" . $channel["version"] . "\" xml:base=\"" . $base_url . "\" " . drupal_attributes($namespaces) . ">\n";
  $output .= format_rss_channel($channel['title'], $channel['link'], $channel['description'], $items, $channel['language'], $channel_extras);
  $output .= "</rss>\n";

  drupal_add_http_header('Content-Type', 'application/rss+xml; charset=utf-8');
  print $output;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
