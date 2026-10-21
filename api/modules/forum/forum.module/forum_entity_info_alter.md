# forum_entity_info_alter()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 217–233 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L217-L233)
- **Module/theme:** forum
- **Implements:** [hook_entity_info_alter()](../../system/system.api.php/hook_entity_info_alter.md)

## Signature

```php
function forum_entity_info_alter(&$info)
```

## Documentation

```text
Implements hook_entity_info_alter().
```

## Code

```php
function forum_entity_info_alter(&$info) {
  // Take over URI construction for taxonomy terms that are forums.
  if ($vid = variable_get('forum_nav_vocabulary', 0)) {
    // Within hook_entity_info(), we can't invoke entity_load() as that would
    // cause infinite recursion, so we call taxonomy_vocabulary_get_names()
    // instead of taxonomy_vocabulary_load(). All we need is the machine name
    // of $vid, so retrieving and iterating all the vocabulary names is somewhat
    // inefficient, but entity info is cached across page requests, and an
    // iteration of all vocabularies once per cache clearing isn't a big deal,
    // and is done as part of taxonomy_entity_info() anyway.
    foreach (taxonomy_vocabulary_get_names() as $machine_name => $vocabulary) {
      if ($vid == $vocabulary->vid) {
        $info['taxonomy_term']['bundles'][$machine_name]['uri callback'] = 'forum_uri';
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
