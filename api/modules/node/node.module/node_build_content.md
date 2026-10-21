# node_build_content()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1392–1447 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1392-L1447)
- **Module/theme:** node

## Signature

```php
function node_build_content($node, $view_mode = 'full', $langcode = NULL)
```

## Documentation

```text
Builds a structured array representing the node's content.

The content built for the node (field values, comments, file attachments or
other node components) will vary depending on the $view_mode parameter.

Drupal core defines the following view modes for nodes, with the following
default use cases:
  - full (default): node is being displayed on its own page (node/123)
  - teaser: node is being displayed on the default home page listing, on
    taxonomy listing pages, or on blog listing pages.
  - rss: node displayed in an RSS feed.
  If search.module is enabled:
  - search_index: node is being indexed for search.
  - search_result: node is being displayed as a search result.
  If book.module is enabled:
  - print: node is being displayed in print-friendly mode.
Contributed modules might define additional view modes, or use existing
view modes in additional contexts.

@param $node
  A node object.
@param $view_mode
  View mode, e.g. 'full', 'teaser'...
@param $langcode
  (optional) A language code to use for rendering. Defaults to the global
  content language of the current request.
```

## Code

```php
function node_build_content($node, $view_mode = 'full', $langcode = NULL) {
  if (!isset($langcode)) {
    $langcode = $GLOBALS['language_content']->language;
  }

  // Remove previously built content, if exists.
  $node->content = array();

  // Allow modules to change the view mode.
  $view_mode = key(entity_view_mode_prepare('node', array($node->nid => $node), $view_mode, $langcode));

  // The 'view' hook can be implemented to overwrite the default function
  // to display nodes.
  if (node_hook($node, 'view')) {
    $node = node_invoke($node, 'view', $view_mode, $langcode);
  }

  // Build fields content.
  // In case of a multiple view, node_view_multiple() already ran the
  // 'prepare_view' step. An internal flag prevents the operation from running
  // twice.
  field_attach_prepare_view('node', array($node->nid => $node), $view_mode, $langcode);
  entity_prepare_view('node', array($node->nid => $node), $langcode);
  $node->content += field_attach_view('node', $node, $view_mode, $langcode);

  // Always display a read more link on teasers because we have no way to know
  // when a teaser view is different than a full view.
  $links = array();
  $node->content['links'] = array(
    '#theme' => 'links__node',
    '#pre_render' => array('drupal_pre_render_links'),
    '#attributes' => array('class' => array('links', 'inline')),
  );
  if ($view_mode == 'teaser') {
    $node_title_stripped = strip_tags($node->title);
    $links['node-readmore'] = array(
      'title' => t('Read more<span class="element-invisible"> about @title</span>', array('@title' => $node_title_stripped)),
      'href' => 'node/' . $node->nid,
      'html' => TRUE,
      'attributes' => array('rel' => 'tag', 'title' => $node_title_stripped),
    );
  }
  $node->content['links']['node'] = array(
    '#theme' => 'links__node__node',
    '#links' => $links,
    '#attributes' => array('class' => array('links', 'inline')),
  );

  // Allow modules to make their own additions to the node.
  module_invoke_all('node_view', $node, $view_mode, $langcode);
  module_invoke_all('entity_view', $node, 'node', $view_mode, $langcode);

  // Make sure the current view mode is stored if no module has already
  // populated the related key.
  $node->content += array('#view_mode' => $view_mode);
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
