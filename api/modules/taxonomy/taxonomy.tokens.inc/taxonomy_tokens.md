# taxonomy_tokens()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.tokens.inc`](_file.md), lines 91–189 · [local source](../../../../source/modules/taxonomy/taxonomy.tokens.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.tokens.inc#L91-L189)
- **Module/theme:** taxonomy
- **Implements:** [hook_tokens()](../../system/system.api.php/hook_tokens.md)

## Signature

```php
function taxonomy_tokens($type, $tokens, array $data = array(), array $options = array())
```

## Documentation

```text
Implements hook_tokens().
```

## Code

```php
function taxonomy_tokens($type, $tokens, array $data = array(), array $options = array()) {
  $replacements = array();
  $sanitize = !empty($options['sanitize']);

  if ($type == 'term' && !empty($data['term'])) {
    $term = $data['term'];

    foreach ($tokens as $name => $original) {
      switch ($name) {
        case 'tid':
          $replacements[$original] = $term->tid;
          break;

        case 'name':
          $replacements[$original] = $sanitize ? check_plain($term->name) : $term->name;
          break;

        case 'description':
          $replacements[$original] = $sanitize ? check_markup($term->description, $term->format, '', TRUE) : $term->description;
          break;

        case 'url':
          $uri = entity_uri('taxonomy_term', $term);
          $replacements[$original] = url($uri['path'], array_merge($uri['options'], array('absolute' => TRUE)));
          break;

        case 'node-count':
          $query = db_select('taxonomy_index');
          $query->condition('tid', $term->tid);
          $query->addTag('term_node_count');
          $count = $query->countQuery()->execute()->fetchField();
          $replacements[$original] = $count;
          break;

        case 'vocabulary':
          $vocabulary = taxonomy_vocabulary_load($term->vid);
          $replacements[$original] = check_plain($vocabulary->name);
          break;

        case 'parent':
          if ($parents = taxonomy_get_parents($term->tid)) {
            $parent = array_pop($parents);
            $replacements[$original] = check_plain($parent->name);
          }
          break;
      }
    }

    if ($vocabulary_tokens = token_find_with_prefix($tokens, 'vocabulary')) {
      $vocabulary = taxonomy_vocabulary_load($term->vid);
      $replacements += token_generate('vocabulary', $vocabulary_tokens, array('vocabulary' => $vocabulary), $options);
    }

    if (($vocabulary_tokens = token_find_with_prefix($tokens, 'parent')) && $parents = taxonomy_get_parents($term->tid)) {
      $parent = array_pop($parents);
      $replacements += token_generate('term', $vocabulary_tokens, array('term' => $parent), $options);
    }
  }

  elseif ($type == 'vocabulary' && !empty($data['vocabulary'])) {
    $vocabulary = $data['vocabulary'];

    foreach ($tokens as $name => $original) {
      switch ($name) {
        case 'vid':
          $replacements[$original] = $vocabulary->vid;
          break;

        case 'name':
          $replacements[$original] = $sanitize ? check_plain($vocabulary->name) : $vocabulary->name;
          break;

        case 'description':
          $replacements[$original] = $sanitize ? filter_xss($vocabulary->description) : $vocabulary->description;
          break;

        case 'term-count':
          $query = db_select('taxonomy_term_data');
          $query->condition('vid', $vocabulary->vid);
          $query->addTag('vocabulary_term_count');
          $count = $query->countQuery()->execute()->fetchField();
          $replacements[$original] = $count;
          break;

        case 'node-count':
          $query = db_select('taxonomy_index', 'ti');
          $query->addExpression('COUNT(DISTINCT ti.nid)');
          $query->leftJoin('taxonomy_term_data', 'td', 'ti.tid = td.tid');
          $query->condition('td.vid', $vocabulary->vid);
          $query->addTag('vocabulary_node_count');
          $count = $query->execute()->fetchField();
          $replacements[$original] = $count;
          break;
      }
    }
  }

  return $replacements;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.tokens.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.tokens.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
