# hook_field_attach_view_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1528–1544 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1528-L1544)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md)

## Signature

```php
function hook_field_attach_view_alter(&$output, $context)
```

## Documentation

```text
Perform alterations on field_attach_view() or field_view_field().

This hook is invoked after the field module has performed the operation.

@param $output
  The structured content array tree for all of the entity's fields.
@param $context
  An associative array containing:
  - entity_type: The type of $entity; for example, 'node' or 'user'.
  - entity: The entity with fields to render.
  - view_mode: View mode; for example, 'full' or 'teaser'.
  - display: Either a view mode string or an array of display settings. If
    this hook is being invoked from field_attach_view(), the 'display'
    element is set to the view mode string. If this hook is being invoked
    from field_view_field(), this element is set to the $display argument
    and the view_mode element is set to '_custom'. See field_view_field()
    for more information on what its $display argument contains.
  - language: The language code used for rendering.
```

## Code

```php
function hook_field_attach_view_alter(&$output, $context) {
  // Append RDF term mappings on displayed taxonomy links.
  foreach (element_children($output) as $field_name) {
    $element = &$output[$field_name];
    if ($element['#field_type'] == 'taxonomy_term_reference' && $element['#formatter'] == 'taxonomy_term_reference_link') {
      foreach ($element['#items'] as $delta => $item) {
        $term = $item['taxonomy_term'];
        if (!empty($term->rdf_mapping['rdftype'])) {
          $element[$delta]['#options']['attributes']['typeof'] = $term->rdf_mapping['rdftype'];
        }
        if (!empty($term->rdf_mapping['name']['predicates'])) {
          $element[$delta]['#options']['attributes']['property'] = $term->rdf_mapping['name']['predicates'];
        }
      }
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_attach_view_alter()".

- [field_test_field_attach_view_alter()](../tests/field_test.module/field_test_field_attach_view_alter.md) — `modules/field/tests/field_test.module`
- [rdf_field_attach_view_alter()](../../rdf/rdf.module/rdf_field_attach_view_alter.md) — `modules/rdf/rdf.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
