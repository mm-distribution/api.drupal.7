# search_help()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 66–97 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L66-L97)
- **Module/theme:** search
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function search_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function search_help($path, $arg) {
  switch ($path) {
    case 'admin/help#search':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Search module provides the ability to index and search for content by exact keywords, and for users by username or e-mail. For more information, see the online handbook entry for <a href="@search-module">Search module</a>.', array('@search-module' => 'http://drupal.org/documentation/modules/search/', '@search' => url('search'))) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Searching content and users') . '</dt>';
      $output .= '<dd>' . t('Users with <em>Use search</em> permission can use the search block and <a href="@search">Search page</a>. Users with the <em>View published content</em> permission can search for content containing exact keywords. Users with the <em>View user profiles</em> permission can search for users containing the keyword anywhere in the user name, and users with the <em>Administer users</em> permission can search for users by email address. Additionally, users with <em>Use advanced search</em> permission can find content using more complex search methods and filtering by choosing the <em>Advanced search</em> option on the <a href="@search">Search page</a>.', array('@search' => url('search'))) . '</dd>';
      $output .= '<dt>' . t('Indexing content with cron') . '</dt>';
      $output .= '<dd>' . t('To provide keyword searching, the search engine maintains an index of words found in the content and its fields, along with text added to your content by other modules (such as comments from the core Comment module, and taxonomy terms from the core Taxonomy module). To build and maintain this index, a correctly configured <a href="@cron">cron maintenance task</a> is required. Users with <em>Administer search</em> permission can further configure the cron settings on the <a href="@searchsettings">Search settings page</a>.', array('@cron' => 'http://drupal.org/cron', '@searchsettings' => url('admin/config/search/settings'))) . '</dd>';
      $output .= '<dt>' . t('Content reindexing') . '</dt>';
      $output .= '<dd>' . t('Content-related actions on your site (creating, editing, or deleting content and comments) automatically cause affected content items to be marked for indexing or reindexing at the next cron run. When content is marked for reindexing, the previous content remains in the index until cron runs, at which time it is replaced by the new content. Unlike content-related actions, actions related to the structure of your site do not cause affected content to be marked for reindexing. Examples of structure-related actions that affect content include deleting or editing taxonomy terms, enabling or disabling modules that add text to content (such as Taxonomy, Comment, and field-providing modules), and modifying the fields or display parameters of your content types. If you take one of these actions and you want to ensure that the search index is updated to reflect your changed site structure, you can mark all content for reindexing by clicking the "Re-index site" button on the <a href="@searchsettings">Search settings page</a>. If you have a lot of content on your site, it may take several cron runs for the content to be reindexed.', array('@searchsettings' => url('admin/config/search/settings'))) . '</dd>';
      $output .= '<dt>' . t('Configuring search settings') . '</dt>';
      $output .= '<dd>' . t('Indexing behavior can be adjusted using the <a href="@searchsettings">Search settings page</a>. Users with <em>Administer search</em> permission can control settings such as the <em>Number of items to index per cron run</em>, <em>Indexing settings</em> (word length), <em>Active search modules</em>, and <em>Content ranking</em>, which lets you adjust the priority in which indexed content is returned in results.', array('@searchsettings' => url('admin/config/search/settings'))) . '</dd>';
      $output .= '<dt>' . t('Search block') . '</dt>';
      $output .= '<dd>' . t('The Search module includes a default <em>Search form</em> block, which can be enabled and configured on the <a href="@blocks">Blocks administration page</a>. The block is available to users with the <em>Search content</em> permission.', array('@blocks' => url('admin/structure/block'))) . '</dd>';
      $output .= '<dt>' . t('Extending Search module') . '</dt>';
      $output .= '<dd>' . t('By default, the Search module only supports exact keyword matching in content searches. You can modify this behavior by installing a language-specific stemming module for your language (such as <a href="http://drupal.org/project/porterstemmer">Porter Stemmer</a> for American English), which allows words such as walk, walking, and walked to be matched in the Search module. Another approach is to use a third-party search technology with stemming or partial word matching features built in, such as <a href="http://drupal.org/project/apachesolr">Apache Solr</a> or <a href="http://drupal.org/project/sphinx">Sphinx</a>. These and other <a href="@contrib-search">search-related contributed modules</a> can be downloaded by visiting Drupal.org.', array('@contrib-search' => 'http://drupal.org/project/modules?filters=tid%3A105')) . '</dd>';
      $output .= '</dl>';
      return $output;
    case 'admin/config/search/settings':
      return '<p>' . t('The search engine maintains an index of words found in your site\'s content. To build and maintain this index, a correctly configured <a href="@cron">cron maintenance task</a> is required. Indexing behavior can be adjusted using the settings below.', array('@cron' => url('admin/reports/status'))) . '</p>';
    case 'search#noresults':
      return t('<ul>
<li>Check if your spelling is correct.</li>
<li>Remove quotes around phrases to search for each word individually. <em>bike shed</em> will often show more results than <em>&quot;bike shed&quot;</em>.</li>
<li>Consider loosening your query with <em>OR</em>. <em>bike OR shed</em> will often show more results than <em>bike shed</em>.</li>
</ul>');
  }
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
