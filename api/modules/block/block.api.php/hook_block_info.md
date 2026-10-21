# hook_block_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/block/block.api.php`](_file.md), lines 105–118 · [local source](../../../../source/modules/block/block.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php#L105-L118)
- **Module/theme:** block
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_block_info()
```

## Documentation

```text
Define all blocks provided by the module.

This hook declares to Drupal what blocks are provided by your module and can
optionally specify initial block configuration settings.

In hook_block_info(), each block your module provides is given a unique
identifier referred to as "delta" (the array key in the return value). Delta
values only need to be unique within your module, and they are used in the
following ways:
- Passed into the other block hooks in your module as an argument to identify
  the block being configured or viewed.
- Used to construct the default HTML ID of "block-MODULE-DELTA" applied to
  each block when it is rendered. This ID may then be used for CSS styling or
  JavaScript programming.
- Used to define a theming template suggestion of block__MODULE__DELTA, for
  advanced theming possibilities.
- Used by other modules to identify your block in hook_block_info_alter() and
  other alter hooks.
The values of delta can be strings or numbers, but because of the uses above
it is preferable to use descriptive strings whenever possible, and only use a
numeric identifier if you have to (for instance if your module allows users
to create several similar blocks that you identify within your module code
with numeric IDs). The maximum length for delta values is 32 bytes.

@return
  An associative array whose keys define the delta for each block and whose
  values contain the block descriptions. Each block description is itself an
  associative array, with the following key-value pairs:
  - info: (required) The human-readable administrative name of the block.
    This is used to identify the block on administration screens, and is not
    displayed to non-administrative users.
  - cache: (optional) A bitmask describing what kind of caching is
    appropriate for the block. Drupal provides the following bitmask
    constants for defining cache granularity:
    - DRUPAL_CACHE_PER_ROLE (default): The block can change depending on the
      roles the user viewing the page belongs to.
    - DRUPAL_CACHE_PER_USER: The block can change depending on the user
      viewing the page. This setting can be resource-consuming for sites with
      large number of users, and should only be used when
      DRUPAL_CACHE_PER_ROLE is not sufficient.
    - DRUPAL_CACHE_PER_PAGE: The block can change depending on the page being
      viewed.
    - DRUPAL_CACHE_GLOBAL: The block is the same for every user on every page
      where it is visible.
    - DRUPAL_CACHE_CUSTOM: The module implements its own caching system.
    - DRUPAL_NO_CACHE: The block should not get cached.
  - properties: (optional) Array of additional metadata to add to the block.
    Common properties include:
    - administrative: Boolean that categorizes this block as usable in an
      administrative context. This might include blocks that help an
      administrator approve/deny comments, or view recently created user
      accounts.
  - weight: (optional) Initial value for the ordering weight of this block.
    Most modules do not provide an initial value, and any value provided can
    be modified by a user on the block configuration screen.
  - status: (optional) Initial value for block enabled status. (1 = enabled,
    0 = disabled). Most modules do not provide an initial value, and any
    value provided can be modified by a user on the block configuration
    screen.
  - region: (optional) Initial value for theme region within which this
    block is set. Most modules do not provide an initial value, and any value
    provided can be modified by a user on the block configuration screen.
    Note: If you set a region that isn't available in the currently enabled
    theme, the block will be disabled.
  - visibility: (optional) Initial value for the visibility flag, which tells
    how to interpret the 'pages' value. Possible values are:
    - BLOCK_VISIBILITY_NOTLISTED: Show on all pages except listed pages.
      'pages' lists the paths where the block should not be shown.
    - BLOCK_VISIBILITY_LISTED: Show only on listed pages. 'pages' lists the
      paths where the block should be shown.
    - BLOCK_VISIBILITY_PHP: Use custom PHP code to determine visibility.
      'pages' gives the PHP code to use.
    Most modules do not provide an initial value for 'visibility' or 'pages',
    and any value provided can be modified by a user on the block
    configuration screen.
  - pages: (optional) See 'visibility' above. A string that contains one or
    more page paths separated by "\n", "\r", or "\r\n" when 'visibility' is
    set to BLOCK_VISIBILITY_NOTLISTED or BLOCK_VISIBILITY_LISTED (example:
    "<front>\nnode/1"), or custom PHP code when 'visibility' is set to
    BLOCK_VISIBILITY_PHP. Paths may use '*' as a wildcard (matching any
    number of characters); '<front>' designates the site's front page. For
    BLOCK_VISIBILITY_PHP, the PHP code's return value should be TRUE if the
    block is to be made visible or FALSE if the block should not be visible.

For a detailed usage example, see block_example.module.

@see hook_block_configure()
@see hook_block_save()
@see hook_block_view()
@see hook_block_info_alter()
```

## Code

```php
function hook_block_info() {
  // This example comes from node.module.
  $blocks['syndicate'] = array(
    'info' => t('Syndicate'),
    'cache' => DRUPAL_NO_CACHE
  );

  $blocks['recent'] = array(
    'info' => t('Recent content'),
    // DRUPAL_CACHE_PER_ROLE will be assumed.
  );

  return $blocks;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_block_info()".

- [aggregator_block_info()](../../aggregator/aggregator.module/aggregator_block_info.md) — `modules/aggregator/aggregator.module`
- [taxonomy_test_block_info()](../../simpletest/tests/taxonomy_test.module/taxonomy_test_block_info.md) — `modules/simpletest/tests/taxonomy_test.module`
- [block_block_info()](../block.module/block_block_info.md) — `modules/block/block.module`
- [block_test_block_info()](../tests/block_test.module/block_test_block_info.md) — `modules/block/tests/block_test.module`
- [blog_block_info()](../../blog/blog.module/blog_block_info.md) — `modules/blog/blog.module`
- [book_block_info()](../../book/book.module/book_block_info.md) — `modules/book/book.module`
- [comment_block_info()](../../comment/comment.module/comment_block_info.md) — `modules/comment/comment.module`
- [forum_block_info()](../../forum/forum.module/forum_block_info.md) — `modules/forum/forum.module`
- [locale_block_info()](../../locale/locale.module/locale_block_info.md) — `modules/locale/locale.module`
- [menu_block_info()](../../menu/menu.module/menu_block_info.md) — `modules/menu/menu.module`
- [node_block_info()](../../node/node.module/node_block_info.md) — `modules/node/node.module`
- [poll_block_info()](../../poll/poll.module/poll_block_info.md) — `modules/poll/poll.module`
- [profile_block_info()](../../profile/profile.module/profile_block_info.md) — `modules/profile/profile.module`
- [search_block_info()](../../search/search.module/search_block_info.md) — `modules/search/search.module`
- [shortcut_block_info()](../../shortcut/shortcut.module/shortcut_block_info.md) — `modules/shortcut/shortcut.module`
- [statistics_block_info()](../../statistics/statistics.module/statistics_block_info.md) — `modules/statistics/statistics.module`
- [system_block_info()](../../system/system.module/system_block_info.md) — `modules/system/system.module`
- [user_block_info()](../../user/user.module/user_block_info.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/block/block.api.php](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
