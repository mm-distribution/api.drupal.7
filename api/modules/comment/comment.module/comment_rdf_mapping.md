# comment_rdf_mapping()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2710–2747 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2710-L2747)
- **Module/theme:** comment
- **Implements:** [hook_rdf_mapping()](../../rdf/rdf.api.php/hook_rdf_mapping.md)

## Signature

```php
function comment_rdf_mapping()
```

## Documentation

```text
Implements hook_rdf_mapping().
```

## Code

```php
function comment_rdf_mapping() {
  return array(
    array(
      'type' => 'comment',
      'bundle' => RDF_DEFAULT_BUNDLE,
      'mapping' => array(
        'rdftype' => array('sioc:Post', 'sioct:Comment'),
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
        'comment_body' => array(
          'predicates' => array('content:encoded'),
        ),
        'pid' => array(
          'predicates' => array('sioc:reply_of'),
          'type' => 'rel',
        ),
        'uid' => array(
          'predicates' => array('sioc:has_creator'),
          'type' => 'rel',
        ),
        'name' => array(
          'predicates' => array('foaf:name'),
        ),
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
