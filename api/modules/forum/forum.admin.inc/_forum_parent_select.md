# _forum_parent_select()

- **Type:** Function
- **File:** [`modules/forum/forum.admin.inc`](_file.md), lines 315–352 · [local source](../../../../source/modules/forum/forum.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc#L315-L352)
- **Module/theme:** forum

## Signature

```php
function _forum_parent_select($tid, $title, $child_type)
```

## Documentation

```text
Returns a select box for available parent terms.

@param $tid
  ID of the term that is being added or edited.
@param $title
  Title for the select box.
@param $child_type
  Whether the child is a forum or a container.

@return
  A select form element.
```

## Code

```php
function _forum_parent_select($tid, $title, $child_type) {

  $parents = taxonomy_get_parents($tid);
  if ($parents) {
    $parent = array_shift($parents);
    $parent = $parent->tid;
  }
  else {
    $parent = 0;
  }

  $vid = variable_get('forum_nav_vocabulary', '');
  $children = taxonomy_get_tree($vid, $tid);

  // A term can't be the child of itself, nor of its children.
  foreach ($children as $child) {
    $exclude[] = $child->tid;
  }
  $exclude[] = $tid;

  $tree = taxonomy_get_tree($vid);
  $options[0] = '<' . t('root') . '>';
  if ($tree) {
    foreach ($tree as $term) {
      if (!in_array($term->tid, $exclude)) {
        $options[$term->tid] = str_repeat(' -- ', $term->depth) . $term->name;
      }
    }
  }
  if ($child_type == 'container') {
    $description = t('Containers are usually placed at the top (root) level, but may also be placed inside another container or forum.');
  }
  elseif ($child_type == 'forum') {
    $description = t('Forums may be placed at the top (root) level, or inside another container or forum.');
  }

  return array('#type' => 'select', '#title' => $title, '#default_value' => $parent, '#options' => $options, '#description' => $description, '#required' => TRUE);
}
```

---
_Drupal 7.103 · [modules/forum/forum.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
