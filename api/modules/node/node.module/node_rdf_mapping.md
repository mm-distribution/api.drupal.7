# node_rdf_mapping()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 839–881 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L839-L881)
- **Module/theme:** node
- **Implements:** [hook_rdf_mapping()](../../rdf/rdf.api.php/hook_rdf_mapping.md)

## Signature

```php
function node_rdf_mapping()
```

## Documentation

```text
Implements hook_rdf_mapping().
```

## Code

```php
function node_rdf_mapping() {
  return array(
    array(
      'type' => 'node',
      'bundle' => RDF_DEFAULT_BUNDLE,
      'mapping' => array(
        'rdftype' => array('sioc:Item', 'foaf:Document'),
        'title' => array(
          'predicates' => array('dc:title'),
        ),
        'created' => array(
          'predicates' => array('dc:date', 'dc:created'),
          'datatype' => 'xsd:dateTime',
          'callback' => 'date_iso8601',
        ),
        'changed' => array(
          'predicates' => array('dc:modified'),
          'datatype' => 'xsd:dateTime',
          'callback' => 'date_iso8601',
        ),
        'body' => array(
          'predicates' => array('content:encoded'),
        ),
        'uid' => array(
          'predicates' => array('sioc:has_creator'),
          'type' => 'rel',
        ),
        'name' => array(
          'predicates' => array('foaf:name'),
        ),
        'comment_count' => array(
          'predicates' => array('sioc:num_replies'),
          'datatype' => 'xsd:integer',
        ),
        'last_activity' => array(
          'predicates' => array('sioc:last_activity_date'),
          'datatype' => 'xsd:dateTime',
          'callback' => 'date_iso8601',
        ),
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
