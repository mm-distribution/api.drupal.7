# rdf_preprocess_node()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 485–538 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L485-L538)
- **Module/theme:** rdf

## Signature

```php
function rdf_preprocess_node(&$variables)
```

## Documentation

```text
Implements MODULE_preprocess_HOOK().
```

## Code

```php
function rdf_preprocess_node(&$variables) {
  // Adds RDFa markup to the node container. The about attribute specifies the
  // URI of the resource described within the HTML element, while the @typeof
  // attribute indicates its RDF type (e.g., foaf:Document, sioc:Person, and so
  // on.)
  $variables['attributes_array']['about'] = empty($variables['node_url']) ? NULL: $variables['node_url'];
  $variables['attributes_array']['typeof'] = empty($variables['node']->rdf_mapping['rdftype']) ? NULL : $variables['node']->rdf_mapping['rdftype'];

  // Adds RDFa markup about the title of the node to the title_suffix.
  if (!empty($variables['node']->rdf_mapping['title']['predicates'])) {
    $variables['title_suffix']['rdf_meta_title'] = array(
      '#theme' => 'rdf_metadata',
      '#metadata' => array(
        array(
          'property' => $variables['node']->rdf_mapping['title']['predicates'],
          'content' => $variables['node']->title,
        ),
      ),
    );
  }

  // Adds RDFa markup for the date.
  if (!empty($variables['rdf_mapping']['created'])) {
    $date_attributes_array = rdf_rdfa_attributes($variables['rdf_mapping']['created'], $variables['created']);
    $variables['rdf_template_variable_attributes_array']['date'] = $date_attributes_array;
    if ($variables['submitted']) {
      $variables['rdf_template_variable_attributes_array']['submitted'] = $date_attributes_array;
    }
  }
  // Adds RDFa markup for the relation between the node and its author.
  if (!empty($variables['rdf_mapping']['uid'])) {
    $variables['rdf_template_variable_attributes_array']['name']['rel'] = $variables['rdf_mapping']['uid']['predicates'];
    if ($variables['submitted']) {
      $variables['rdf_template_variable_attributes_array']['submitted']['rel'] = $variables['rdf_mapping']['uid']['predicates'];
    }
  }

  // Adds RDFa markup annotating the number of comments a node has.
  if (isset($variables['node']->comment_count) &&
      !empty($variables['node']->rdf_mapping['comment_count']['predicates']) &&
      user_access('access comments')) {
    // Adds RDFa markup for the comment count near the node title as metadata.
    $variables['title_suffix']['rdf_meta_comment_count'] = array(
      '#theme' => 'rdf_metadata',
      '#metadata' => array(
        array(
          'property' => $variables['node']->rdf_mapping['comment_count']['predicates'],
          'content' => $variables['node']->comment_count,
          'datatype' => $variables['node']->rdf_mapping['comment_count']['datatype'],
        ),
      ),
    );
  }
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
