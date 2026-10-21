# system_update_7004()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2003–2049 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2003-L2049)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7004(&$sandbox)
```

## Documentation

```text
Remove hardcoded numeric deltas from all blocks in core.
```

## Code

```php
function system_update_7004(&$sandbox) {
  // Get an array of the renamed block deltas, organized by module.
  $renamed_deltas = array(
    'blog' => array('0' => 'recent'),
    'book' => array('0' => 'navigation'),
    'comment' => array('0' => 'recent'),
    'forum' => array(
      '0' => 'active',
      '1' => 'new',
    ),
    'locale' => array('0' => LANGUAGE_TYPE_INTERFACE),
    'node' => array('0' => 'syndicate'),
    'poll' => array('0' => 'recent'),
    'profile' => array('0' => 'author-information'),
    'search' => array('0' => 'form'),
    'statistics' => array('0' => 'popular'),
    'system' => array('0' => 'powered-by'),
    'user' => array(
      '0' => 'login',
      '1' => 'navigation',
      '2' => 'new',
      '3' => 'online',
    ),
  );

  $moved_deltas = array(
    'user' => array('navigation' => 'system'),
  );

  // Only run this the first time through the batch update.
  if (!isset($sandbox['progress'])) {
    // Rename forum module's block variables.
    $forum_block_num_0 = variable_get('forum_block_num_0');
    if (isset($forum_block_num_0)) {
      variable_set('forum_block_num_active', $forum_block_num_0);
      variable_del('forum_block_num_0');
    }
    $forum_block_num_1 = variable_get('forum_block_num_1');
    if (isset($forum_block_num_1)) {
      variable_set('forum_block_num_new', $forum_block_num_1);
      variable_del('forum_block_num_1');
    }
  }

  update_fix_d7_block_deltas($sandbox, $renamed_deltas, $moved_deltas);

}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
