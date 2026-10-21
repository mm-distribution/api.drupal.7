# toolbar_view()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 189–284 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L189-L284)
- **Module/theme:** toolbar

## Signature

```php
function toolbar_view()
```

## Documentation

```text
Builds the admin menu as a structured array ready for drupal_render().

@return
  Array of links and settings relating to the admin menu.
```

## Code

```php
function toolbar_view() {
  global $user;

  $module_path = drupal_get_path('module', 'toolbar');
  $build = array(
    '#theme' => 'toolbar',
    '#attached'=> array(
      'js' => array(
        $module_path . '/toolbar.js',
        array(
          'data' => array('tableHeaderOffset' => 'Drupal.toolbar.height'),
          'type' => 'setting'
        ),
      ),
      'css' => array(
        $module_path . '/toolbar.css',
        $module_path . '/toolbar-print.css' => array(
          'media' => 'print',
        ),
      ),
      'library' => array(array('system', 'jquery.cookie')),
    ),
  );

  // Retrieve the admin menu from the database.
  $links = toolbar_menu_navigation_links(toolbar_get_menu_tree());
  $build['toolbar_menu'] = array(
    '#theme' => 'links__toolbar_menu',
    '#links' => $links,
    '#attributes' => array('id' => 'toolbar-menu'),
    '#heading' => array('text' => t('Administrative toolbar'), 'level' => 'h2', 'class' => 'element-invisible'),
  );

  // Add logout & user account links or login link.
  if ($user->uid) {
    $links = array(
      'account' => array(
        'title' => t('Hello <strong>@username</strong>', array('@username' => format_username($user))),
        'href' => 'user',
        'html' => TRUE,
        'attributes' => array('title' => t('User account')),
      ),
      'logout' => array(
        'title' => t('Log out'),
        'href' => 'user/logout',
      ),
    );
  }
  else {
     $links = array(
      'login' => array(
        'title' => t('Log in'),
        'href' => 'user',
      ),
    );
  }
  $build['toolbar_user'] = array(
    '#theme' => 'links__toolbar_user',
    '#links' => $links,
    '#attributes' => array('id' => 'toolbar-user'),
  );

  // Add a "home" link.
  $link = array(
    'home' => array(
      'title' => '<span class="home-link">Home</span>',
      'href' => '<front>',
      'html' => TRUE,
      'attributes' => array('title' => t('Home')),
    ),
  );
  $build['toolbar_home'] = array(
    '#theme' => 'links',
    '#links' => $link,
    '#attributes' => array('id' => 'toolbar-home'),
  );

  // Add an anchor to be able to toggle the visibility of the drawer.
  $build['toolbar_toggle'] = array(
    '#theme' => 'toolbar_toggle',
    '#collapsed' => _toolbar_is_collapsed(),
    '#attributes' => array('class' => array('toggle')),
  );

  // Prepare the drawer links CSS classes.
  $toolbar_drawer_classes = array(
    'toolbar-drawer',
    'clearfix',
  );
  if(_toolbar_is_collapsed()) {
    $toolbar_drawer_classes[] = 'collapsed';
  }
  $build['toolbar_drawer_classes'] = implode(' ', $toolbar_drawer_classes);

  return $build;
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
