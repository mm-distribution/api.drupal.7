# taxonomy_field_formatter_view()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1593–1644 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1593-L1644)
- **Module/theme:** taxonomy
- **Implements:** [hook_field_formatter_view()](../../field/field.api.php/hook_field_formatter_view.md)

## Signature

```php
function taxonomy_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display)
```

## Documentation

```text
Implements hook_field_formatter_view().
```

## Code

```php
function taxonomy_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display) {
  $element = array();

  // Terms whose tid is 'autocreate' do not exist
  // yet and $item['taxonomy_term'] is not set. Theme such terms as
  // just their name.

  switch ($display['type']) {
    case 'taxonomy_term_reference_link':
      foreach ($items as $delta => $item) {
        if ($item['tid'] === 'autocreate') {
          $element[$delta] = array(
            '#markup' => check_plain($item['name']),
          );
        }
        else {
          $term = $item['taxonomy_term'];
          $uri = entity_uri('taxonomy_term', $term);
          $element[$delta] = array(
            '#type' => 'link',
            '#title' => $term->name,
            '#href' => $uri['path'],
            '#options' => $uri['options'],
          );
        }
      }
      break;

    case 'taxonomy_term_reference_plain':
      foreach ($items as $delta => $item) {
        $name = ($item['tid'] !== 'autocreate' ? $item['taxonomy_term']->name : $item['name']);
        $element[$delta] = array(
          '#markup' => check_plain($name),
        );
      }
      break;

    case 'taxonomy_term_reference_rss_category':
      foreach ($items as $delta => $item) {
        $entity->rss_elements[] = array(
          'key' => 'category',
          'value' => $item['tid'] !== 'autocreate' ? $item['taxonomy_term']->name : $item['name'],
          'attributes' => array(
            'domain' => $item['tid'] !== 'autocreate' ? url('taxonomy/term/' . $item['tid'], array('absolute' => TRUE)) : '',
          ),
        );
      }
      break;
  }

  return $element;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
