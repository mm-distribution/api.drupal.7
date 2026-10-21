# SystemAdminTestCase::testAdminPages()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2845–2906 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2845-L2906)
- **Class:** [SystemAdminTestCase](../SystemAdminTestCase.md)
- **Module/theme:** system

## Signature

```php
function testAdminPages()
```

## Documentation

```text
Tests output on administrative listing pages.
```

## Code

```php
  function testAdminPages() {
    // Go to Administration.
    $this->drupalGet('admin');

    // Verify that all visible, top-level administration links are listed on
    // the main administration page.
    foreach (menu_get_router() as $path => $item) {
      if (strpos($path, 'admin/') === 0 && ($item['type'] & MENU_VISIBLE_IN_TREE) && $item['_number_parts'] == 2) {
        $this->assertLink($item['title']);
        $this->assertLinkByHref($path);
        $this->assertText($item['description']);
      }
    }

    // For each administrative listing page on which the Locale module appears,
    // verify that there are links to the module's primary configuration pages,
    // but no links to its individual sub-configuration pages. Also verify that
    // a user with access to only some Locale module administration pages only
    // sees links to the pages they have access to.
    $admin_list_pages = array(
      'admin/index',
      'admin/config',
      'admin/config/regional',
    );

    foreach ($admin_list_pages as $page) {
      // For the administrator, verify that there are links to Locale's primary
      // configuration pages, but no links to individual sub-configuration
      // pages.
      $this->drupalLogin($this->admin_user);
      $this->drupalGet($page);
      $this->assertLinkByHref('admin/config');
      $this->assertLinkByHref('admin/config/regional/settings');
      $this->assertLinkByHref('admin/config/regional/date-time');
      $this->assertLinkByHref('admin/config/regional/language');
      $this->assertNoLinkByHref('admin/config/regional/language/configure/session');
      $this->assertNoLinkByHref('admin/config/regional/language/configure/url');
      $this->assertLinkByHref('admin/config/regional/translate');
      // On admin/index only, the administrator should also see a "Configure
      // permissions" link for the Locale module.
      if ($page == 'admin/index') {
        $this->assertLinkByHref("admin/people/permissions#module-locale");
      }

      // For a less privileged user, verify that there are no links to Locale's
      // primary configuration pages, but a link to the translate page exists.
      $this->drupalLogin($this->web_user);
      $this->drupalGet($page);
      $this->assertLinkByHref('admin/config');
      $this->assertNoLinkByHref('admin/config/regional/settings');
      $this->assertNoLinkByHref('admin/config/regional/date-time');
      $this->assertNoLinkByHref('admin/config/regional/language');
      $this->assertNoLinkByHref('admin/config/regional/language/configure/session');
      $this->assertNoLinkByHref('admin/config/regional/language/configure/url');
      $this->assertLinkByHref('admin/config/regional/translate');
      // This user cannot configure permissions, so even on admin/index should
      // not see a "Configure permissions" link for the Locale module.
      if ($page == 'admin/index') {
        $this->assertNoLinkByHref("admin/people/permissions#module-locale");
      }
    }
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
