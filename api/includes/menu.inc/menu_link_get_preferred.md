# menu_link_get_preferred()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2480–2563 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2480-L2563)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_link_get_preferred($path = NULL, $selected_menu = NULL)
```

## Documentation

```text
Looks up the preferred menu link for a given system path.

@param $path
  The path; for example, 'node/5'. The function will find the corresponding
  menu link ('node/5' if it exists, or fallback to 'node/%').
@param $selected_menu
  The name of a menu used to restrict the search for a preferred menu link.
  If not specified, all the menus returned by menu_get_active_menu_names()
  will be used.

@return
  A fully translated menu link, or FALSE if no matching menu link was
  found. The most specific menu link ('node/5' preferred over 'node/%') in
  the most preferred menu (as defined by menu_get_active_menu_names()) is
  returned.
```

## Code

```php
function menu_link_get_preferred($path = NULL, $selected_menu = NULL) {
  $preferred_links = &drupal_static(__FUNCTION__);

  if (!isset($path)) {
    $path = $_GET['q'];
  }

  if (empty($selected_menu)) {
    // Use an illegal menu name as the key for the preferred menu link.
    $selected_menu = MENU_PREFERRED_LINK;
  }

  if (!isset($preferred_links[$path])) {
    // Look for the correct menu link by building a list of candidate paths,
    // which are ordered by priority (translated hrefs are preferred over
    // untranslated paths). Afterwards, the most relevant path is picked from
    // the menus, ordered by menu preference.
    $item = menu_get_item($path);
    if ($item === FALSE) {
      return FALSE;
    }
    $path_candidates = array();
    // 1. The current item href.
    $path_candidates[$item['href']] = $item['href'];
    // 2. The tab root href of the current item (if any).
    if ($item['tab_parent'] && ($tab_root = menu_get_item($item['tab_root_href']))) {
      $path_candidates[$tab_root['href']] = $tab_root['href'];
    }
    // 3. The current item path (with wildcards).
    $path_candidates[$item['path']] = $item['path'];
    // 4. The tab root path of the current item (if any).
    if (!empty($tab_root)) {
      $path_candidates[$tab_root['path']] = $tab_root['path'];
    }

    // Retrieve a list of menu names, ordered by preference.
    $menu_names = menu_get_active_menu_names();
    // Put the selected menu at the front of the list.
    array_unshift($menu_names, $selected_menu);

    $query = db_select('menu_links', 'ml', array('fetch' => PDO::FETCH_ASSOC));
    $query->leftJoin('menu_router', 'm', 'm.path = ml.router_path');
    $query->fields('ml');
    // Weight must be taken from {menu_links}, not {menu_router}.
    $query->addField('ml', 'weight', 'link_weight');
    $query->fields('m');
    $query->condition('ml.link_path', $path_candidates, 'IN');
    $query->addTag('preferred_menu_links');

    // Sort candidates by link path and menu name.
    $candidates = array();
    foreach ($query->execute() as $candidate) {
      $candidate['weight'] = $candidate['link_weight'];
      $candidates[$candidate['link_path']][$candidate['menu_name']] = $candidate;
      // Add any menus not already in the menu name search list.
      if (!in_array($candidate['menu_name'], $menu_names)) {
        $menu_names[] = $candidate['menu_name'];
      }
    }

    // Store the most specific link for each menu. Also save the most specific
    // link of the most preferred menu in $preferred_link.
    foreach ($path_candidates as $link_path) {
      if (isset($candidates[$link_path])) {
        foreach ($menu_names as $menu_name) {
          if (empty($preferred_links[$path][$menu_name]) && isset($candidates[$link_path][$menu_name])) {
            $candidate_item = $candidates[$link_path][$menu_name];
            $map = explode('/', $path);
            _menu_translate($candidate_item, $map);
            if ($candidate_item['access']) {
              $preferred_links[$path][$menu_name] = $candidate_item;
              if (empty($preferred_links[$path][MENU_PREFERRED_LINK])) {
                // Store the most specific link.
                $preferred_links[$path][MENU_PREFERRED_LINK] = $candidate_item;
              }
            }
          }
        }
      }
    }
  }

  return isset($preferred_links[$path][$selected_menu]) ? $preferred_links[$path][$selected_menu] : FALSE;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
