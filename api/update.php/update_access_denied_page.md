# update_access_denied_page()

- **Type:** Function
- **File:** [`update.php`](_file.md), lines 281–292 · [local source](../../source/update.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/update.php#L281-L292)

## Signature

```php
function update_access_denied_page()
```

## Documentation

```text
Renders a 403 access denied page for update.php.

@return
  Rendered HTML warning with 403 status.
```

## Code

```php
function update_access_denied_page() {
  drupal_add_http_header('Status', '403 Forbidden');
  watchdog('access denied', 'update.php', NULL, WATCHDOG_WARNING);
  drupal_set_title('Access denied');
  return '<p>Access denied. You are not authorized to access this page. Log in using either an account with the <em>administer software updates</em> permission or the site maintenance account (the account you created during installation). If you cannot log in, you will have to edit <code>settings.php</code> to bypass this access check. To do this:</p>
<ol>
 <li>With a text editor find the settings.php file on your system. From the main Drupal directory that you installed all the files into, go to <code>sites/your_site_name</code> if such directory exists, or else to <code>sites/default</code> which applies otherwise.</li>
 <li>There is a line inside your settings.php file that says <code>$update_free_access = FALSE;</code>. Change it to <code>$update_free_access = TRUE;</code>.</li>
 <li>As soon as the update.php script is done, you must change the settings.php file back to its original form with <code>$update_free_access = FALSE;</code>.</li>
 <li>To avoid having this problem in the future, remember to log in to your website using either an account with the <em>administer software updates</em> permission or the site maintenance account (the account you created during installation) before you backup your database at the beginning of the update process.</li>
</ol>';
}
```

---
_Drupal 7.103 · [update.php](https://github.com/drupal/drupal/blob/7.103/update.php) · Licensed GPL-2.0-or-later (see LICENSE)._
