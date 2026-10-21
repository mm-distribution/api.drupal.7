# book_help()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 11–33 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L11-L33)
- **Module/theme:** book
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function book_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function book_help($path, $arg) {
  switch ($path) {
    case 'admin/help#book':
      $output = '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Book module is used for creating structured, multi-page content, such as site resource guides, manuals, and wikis. It allows you to create content that has chapters, sections, subsections, or any similarly-tiered structure. For more information, see the online handbook entry for <a href="@book">Book module</a>.', array('@book' => 'http://drupal.org/documentation/modules/book/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Adding and managing book content') . '</dt>';
      $output .= '<dd>' . t('You can assign separate permissions for <em>creating</em>, <em>editing</em>, and <em>deleting</em> book content, as well as <em>adding content to books</em>, and <em>creating new books</em>. Users with the <em>Administer book outlines</em> permission can add <em>any</em> type of content to a book by selecting the appropriate book outline while editing the content. They can also view a list of all books, and edit and rearrange section titles on the <a href="@admin-book">Book administration page</a>.', array('@admin-book' => url('admin/content/book'))) . '</dd>';
      $output .= '<dt>' . t('Book navigation') . '</dt>';
      $output .= '<dd>' . t("Book pages have a default book-specific navigation block. This navigation block contains links that lead to the previous and next pages in the book, and to the level above the current page in the book's structure. This block can be enabled on the <a href='@admin-block'>Blocks administration page</a>. For book pages to show up in the book navigation, they must be added to a book outline.", array('@admin-block' => url('admin/structure/block'))) . '</dd>';
      $output .= '<dt>' . t('Collaboration') . '</dt>';
      $output .= '<dd>' . t('Books can be created collaboratively, as they allow users with appropriate permissions to add pages into existing books, and add those pages to a custom table of contents menu.') . '</dd>';
      $output .= '<dt>' . t('Printing books') . '</dt>';
      $output .= '<dd>' . t("Users with the <em>View printer-friendly books</em> permission can select the <em>printer-friendly version</em> link visible at the bottom of a book page's content to generate a printer-friendly display of the page and all of its subsections.") . '</dd>';
      $output .= '</dl>';
      return $output;
    case 'admin/content/book':
      return '<p>' . t('The book module offers a means to organize a collection of related content pages, collectively known as a book. When viewed, this content automatically displays links to adjacent book pages, providing a simple navigation system for creating and reviewing structured content.') . '</p>';
    case 'node/%/outline':
      return '<p>' . t('The outline feature allows you to include pages in the <a href="@book">Book hierarchy</a>, as well as move them within the hierarchy or to <a href="@book-admin">reorder an entire book</a>.', array('@book' => url('book'), '@book-admin' => url('admin/content/book'))) . '</p>';
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
