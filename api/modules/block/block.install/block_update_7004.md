# block_update_7004()

- **Type:** Function
- **File:** [`modules/block/block.install`](_file.md), lines 252–406 · [local source](../../../../source/modules/block/block.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install#L252-L406)
- **Module/theme:** block
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function block_update_7004()
```

## Documentation

```text
Add new blocks to new regions, migrate custom variables to blocks.
```

## Code

```php
function block_update_7004() {
  // Collect a list of themes with blocks.
  $themes_with_blocks = array();
  $result = db_query("SELECT s.name FROM {system} s INNER JOIN {block} b ON s.name = b.theme WHERE s.type = 'theme' GROUP by s.name");

  $insert = db_insert('block')->fields(array('module', 'delta', 'theme', 'status', 'weight', 'region', 'pages', 'cache'));
  foreach ($result as $theme) {
    $themes_with_blocks[] = $theme->name;
    // Add new system generated help block.
    $insert->values(array(
      'module' => 'system',
      'delta' => 'help',
      'theme' => $theme->name,
      'status' => 1,
      'weight' => 0,
      'region' => 'help',
      'pages' => '',
      'cache' => DRUPAL_CACHE_PER_ROLE,
    ));
    // Add new system generated main page content block.
    $insert->values(array(
      'module' => 'system',
      'delta' => 'main',
      'theme' => $theme->name,
      'status' => 1,
      'weight' => 0,
      'region' => 'content',
      'pages' => '',
      'cache' => DRUPAL_NO_CACHE,
    ));
  }
  $insert->execute();

  // Migrate blocks from left/right regions to first/second regions.
  db_update('block')
    ->fields(array('region' => 'sidebar_first'))
    ->condition('region', 'left')
    ->execute();
  db_update('block')
    ->fields(array('region' => 'sidebar_second'))
    ->condition('region', 'right')
    ->execute();

  // Migrate contact form information.
  $default_format = variable_get('filter_default_format', 1);
  if ($contact_help = variable_get('contact_form_information', '')) {
    $bid = db_insert('block_custom')
      ->fields(array(
        'body' => $contact_help,
        'info' => 'Contact page help',
        'format' => $default_format,
      ))
      ->execute();

    $insert = db_insert('block')->fields(array('module', 'delta', 'theme', 'status', 'weight', 'region', 'visibility', 'pages', 'cache'));
    foreach ($themes_with_blocks as $theme) {
      // Add contact help block for themes, which had blocks.
      $insert->values(array(
        'module' => 'block',
        'delta' => $bid,
        'theme' => $theme,
        'status' => 1,
        'weight' => 5,
        'region' => 'help',
        'visibility' => BLOCK_VISIBILITY_LISTED,
        'pages' => 'contact',
        'cache' => DRUPAL_NO_CACHE,
      ));
    }
    drupal_set_message('The contact form information setting was migrated to <a href="' . url('admin/structure/block/manage/block/' . $bid . '/configure') . '">a custom block</a> and set up to only show on the site-wide contact page. The block was set to use the default text format, which might differ from the HTML based format used before. Check the block and ensure that the output is right.');
  }
  $insert->execute();

  // Migrate user help setting.
  if ($user_help = variable_get('user_registration_help', '')) {
    $bid = db_insert('block_custom')->fields(array('body' => $user_help, 'info' => 'User registration guidelines', 'format' => $default_format))->execute();

    $insert = db_insert('block')->fields(array('module', 'delta', 'theme', 'status', 'weight', 'region', 'visibility', 'pages', 'cache'));
    foreach ($themes_with_blocks as $theme) {
      // Add user registration help block for themes, which had blocks.
      $insert->values(array(
        'module' => 'block',
        'delta' => $bid,
        'theme' => $theme,
        'status' => 1,
        'weight' => 5,
        'region' => 'help',
        'visibility' => BLOCK_VISIBILITY_LISTED,
        'pages' => 'user/register',
        'cache' => DRUPAL_NO_CACHE,
      ));
    }
    drupal_set_message('The user registration guidelines were migrated to <a href="' . url('admin/structure/block/manage/block/' . $bid . '/configure') . '">a custom block</a> and set up to only show on the user registration page. The block was set to use the default text format, which might differ from the HTML based format used before. Check the block and ensure that the output is right.');
    $insert->execute();
  }

  // Migrate site mission setting.
  if ($mission = variable_get('site_mission')) {
    $bid = db_insert('block_custom')->fields(array('body' => $mission, 'info' => 'Site mission', 'format' => $default_format))->execute();

    $insert = db_insert('block')->fields(array('module', 'delta', 'theme', 'status', 'weight', 'region', 'visibility', 'pages', 'cache'));
    foreach ($themes_with_blocks as $theme) {
      // Add mission block for themes, which had blocks.
      $insert->values(array(
        'module' => 'block',
        'delta' => $bid,
        'theme' => $theme,
        'status' => 1,
        'weight' => 0,
        'region' => 'highlighted',
        'visibility' => BLOCK_VISIBILITY_LISTED,
        'pages' => '<front>',
        'cache' => DRUPAL_NO_CACHE,
      ));
    }
    drupal_set_message('The site mission was migrated to <a href="' . url('admin/structure/block/manage/block/' . $bid . '/configure') . '">a custom block</a> and set up to only show on the front page in the highlighted content region. The block was set to use the default text format, which might differ from the HTML based format used before. Check the block and ensure that the output is right. If your theme does not have a highlighted content region, you might need to <a href="' . url('admin/structure/block') . '">relocate the block</a>.');
    $insert->execute();
    // Migrate mission to RSS site description.
    variable_set('feed_description', $mission);
  }

  // Migrate site footer message to a custom block.
  if ($footer_message = variable_get('site_footer', '')) {
    $bid = db_insert('block_custom')->fields(array('body' => $footer_message, 'info' => 'Footer message', 'format' => $default_format))->execute();

    $insert = db_insert('block')->fields(array('module', 'delta', 'theme', 'status', 'weight', 'region', 'pages', 'cache'));
    foreach ($themes_with_blocks as $theme) {
      // Add site footer block for themes, which had blocks.
      // Set low weight, so the block comes early (it used to be
      // before the other blocks).
      $insert->values(array(
        'module' => 'block',
        'delta' => $bid,
        'theme' => $theme,
        'status' => 1,
        'weight' => -10,
        'region' => 'footer',
        'pages' => '',
        'cache' => DRUPAL_NO_CACHE,
      ));
    }
    drupal_set_message('The footer message was migrated to <a href="' . url('admin/structure/block/manage/block/' . $bid . '/configure') . '">a custom block</a> and set up to appear in the footer. The block was set to use the default text format, which might differ from the HTML based format used before. Check the block and ensure that the output is right. If your theme does not have a footer region, you might need to <a href="' . url('admin/structure/block') . '">relocate the block</a>.');
    $insert->execute();
  }

  // Remove the variables (even if they were saved empty on the admin interface),
  // to avoid keeping clutter in the variables table.
  variable_del('contact_form_information');
  variable_del('user_registration_help');
  variable_del('site_mission');
  variable_del('site_footer');

  // Rebuild theme data, so the new 'help' region is identified.
  system_rebuild_theme_data();
}
```

---
_Drupal 7.103 · [modules/block/block.install](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install) · Licensed GPL-2.0-or-later (see LICENSE)._
