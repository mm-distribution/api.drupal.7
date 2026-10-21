# node_token_info()

- **Type:** Function
- **File:** [`modules/node/node.tokens.inc`](_file.md), lines 13–87 · [local source](../../../../source/modules/node/node.tokens.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.tokens.inc#L13-L87)
- **Module/theme:** node
- **Implements:** [hook_token_info()](../../system/system.api.php/hook_token_info.md)

## Signature

```php
function node_token_info()
```

## Documentation

```text
Implements hook_token_info().
```

## Code

```php
function node_token_info() {
  $type = array(
    'name' => t('Nodes'),
    'description' => t('Tokens related to individual content items, or "nodes".'),
    'needs-data' => 'node',
  );

  // Core tokens for nodes.
  $node['nid'] = array(
    'name' => t("Content ID"),
    'description' => t('The unique ID of the content item, or "node".'),
  );
  $node['vid'] = array(
    'name' => t("Revision ID"),
    'description' => t("The unique ID of the node's latest revision."),
  );
  $node['tnid'] = array(
    'name' => t("Translation set ID"),
    'description' => t("The unique ID of the original-language version of this node, if one exists."),
  );
  $node['type'] = array(
    'name' => t("Content type"),
    'description' => t("The type of the node."),
  );
  $node['type-name'] = array(
    'name' => t("Content type name"),
    'description' => t("The human-readable name of the node type."),
  );
  $node['title'] = array(
    'name' => t("Title"),
    'description' => t("The title of the node."),
  );
  $node['body'] = array(
    'name' => t("Body"),
    'description' => t("The main body text of the node."),
  );
  $node['summary'] = array(
    'name' => t("Summary"),
    'description' => t("The summary of the node's main body text."),
  );
  $node['language'] = array(
    'name' => t("Language"),
    'description' => t("The language the node is written in."),
  );
  $node['url'] = array(
    'name' => t("URL"),
    'description' => t("The URL of the node."),
  );
  $node['edit-url'] = array(
    'name' => t("Edit URL"),
    'description' => t("The URL of the node's edit page."),
  );

  // Chained tokens for nodes.
  $node['created'] = array(
    'name' => t("Date created"),
    'description' => t("The date the node was posted."),
    'type' => 'date',
  );
  $node['changed'] = array(
    'name' => t("Date changed"),
    'description' => t("The date the node was most recently updated."),
    'type' => 'date',
  );
  $node['author'] = array(
    'name' => t("Author"),
    'description' => t("The author of the node."),
    'type' => 'user',
  );

  return array(
    'types' => array('node' => $type),
    'tokens' => array('node' => $node),
  );
}
```

---
_Drupal 7.103 · [modules/node/node.tokens.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.tokens.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
