# rdf_preprocess_comment()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 665–718 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L665-L718)
- **Module/theme:** rdf

## Signature

```php
function rdf_preprocess_comment(&$variables)
```

## Documentation

```text
Implements MODULE_preprocess_HOOK().
```

## Code

```php
function rdf_preprocess_comment(&$variables) {
  $comment = $variables['comment'];
  if (!empty($comment->rdf_mapping['rdftype'])) {
    // Adds RDFa markup to the comment container. The about attribute specifies
    // the URI of the resource described within the HTML element, while the
    // typeof attribute indicates its RDF type (e.g., sioc:Post, foaf:Document,
    // and so on.)
    $uri = entity_uri('comment', $comment);
    $variables['attributes_array']['about'] = url($uri['path'], $uri['options']);
    $variables['attributes_array']['typeof'] = $comment->rdf_mapping['rdftype'];
  }

  // Adds RDFa markup for the date of the comment.
  if (!empty($comment->rdf_mapping['created'])) {
    // The comment date is precomputed as part of the rdf_data so that it can be
    // cached as part of the entity.
    $date_attributes_array = $comment->rdf_data['date'];
    $variables['rdf_template_variable_attributes_array']['created'] = $date_attributes_array;
    $variables['rdf_template_variable_attributes_array']['submitted'] = $date_attributes_array;
  }
  // Adds RDFa markup for the relation between the comment and its author.
  if (!empty($comment->rdf_mapping['uid'])) {
    $variables['rdf_template_variable_attributes_array']['author']['rel'] = $comment->rdf_mapping['uid']['predicates'];
    $variables['rdf_template_variable_attributes_array']['submitted']['rel'] = $comment->rdf_mapping['uid']['predicates'];
  }
  if (!empty($comment->rdf_mapping['title'])) {
    // Adds RDFa markup to the subject of the comment. Because the RDFa markup
    // is added to an <h3> tag which might contain HTML code, we specify an
    // empty datatype to ensure the value of the title read by the RDFa parsers
    // is a literal.
    $variables['title_attributes_array']['property'] = $comment->rdf_mapping['title']['predicates'];
    $variables['title_attributes_array']['datatype'] = '';
  }

  // Annotates the parent relationship between the current comment and the node
  // it belongs to. If available, the parent comment is also annotated.
  if (!empty($comment->rdf_mapping['pid'])) {
    // Adds the relation to the parent node.
    $parent_node_attributes['rel'] = $comment->rdf_mapping['pid']['predicates'];
    // The parent node URI is precomputed as part of the rdf_data so that it can
    // be cached as part of the entity.
    $parent_node_attributes['resource'] = $comment->rdf_data['nid_uri'];
    $variables['rdf_metadata_attributes_array'][] = $parent_node_attributes;

    // Adds the relation to parent comment, if it exists.
    if ($comment->pid != 0) {
      $parent_comment_attributes['rel'] = $comment->rdf_mapping['pid']['predicates'];
      // The parent comment URI is precomputed as part of the rdf_data so that
      // it can be cached as part of the entity.
      $parent_comment_attributes['resource'] = $comment->rdf_data['pid_uri'];
      $variables['rdf_metadata_attributes_array'][] = $parent_comment_attributes;
    }
  }
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
