# aggregator_help()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 16–45 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L16-L45)
- **Module/theme:** aggregator
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function aggregator_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function aggregator_help($path, $arg) {
  switch ($path) {
    case 'admin/help#aggregator':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Aggregator module is an on-site syndicator and news reader that gathers and displays fresh content from RSS-, RDF-, and Atom-based feeds made available across the web. Thousands of sites (particularly news sites and blogs) publish their latest headlines in feeds, using a number of standardized XML-based formats. For more information, see the online handbook entry for <a href="@aggregator-module">Aggregator module</a>.', array('@aggregator-module' => 'http://drupal.org/documentation/modules/aggregator', '@aggregator' => url('aggregator'))) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Viewing feeds') . '</dt>';
      $output .= '<dd>' . t('Feeds contain published content, and may be grouped in categories, generally by topic. Users view feed content in the <a href="@aggregator">main aggregator display</a>, or by <a href="@aggregator-sources">their source</a> (usually via an RSS feed reader). The most recent content in a feed or category can be displayed as a block through the <a href="@admin-block">Blocks administration page</a>.', array('@aggregator' => url('aggregator'), '@aggregator-sources' => url('aggregator/sources'), '@admin-block' => url('admin/structure/block'))) . '</a></dd>';
      $output .= '<dt>' . t('Adding, editing, and deleting feeds') . '</dt>';
      $output .= '<dd>' . t('Administrators can add, edit, and delete feeds, and choose how often to check each feed for newly updated items on the <a href="@feededit">Feed aggregator administration page</a>.', array('@feededit' => url('admin/config/services/aggregator'))) . '</dd>';
      $output .= '<dt>' . t('OPML integration') . '</dt>';
      $output .= '<dd>' . t('A <a href="@aggregator-opml">machine-readable OPML file</a> of all feeds is available. OPML is an XML-based file format used to share outline-structured information such as a list of RSS feeds. Feeds can also be <a href="@import-opml">imported via an OPML file</a>.', array('@aggregator-opml' => url('aggregator/opml'), '@import-opml' => url('admin/config/services/aggregator'))) . '</dd>';
      $output .= '<dt>' . t('Configuring cron') . '</dt>';
      $output .= '<dd>' . t('A correctly configured <a href="@cron">cron maintenance task</a> is required to update feeds automatically.', array('@cron' => 'http://drupal.org/cron')) . '</dd>';
      $output .= '</dl>';
      return $output;
    case 'admin/config/services/aggregator':
      $output = '<p>' . t('Thousands of sites (particularly news sites and blogs) publish their latest headlines and posts in feeds, using a number of standardized XML-based formats. Formats supported by the aggregator include <a href="@rss">RSS</a>, <a href="@rdf">RDF</a>, and <a href="@atom">Atom</a>.', array('@rss' => 'http://cyber.law.harvard.edu/rss/', '@rdf' => 'http://www.w3.org/RDF/', '@atom' => 'http://www.atomenabled.org')) . '</p>';
      $output .= '<p>' . t('Current feeds are listed below, and <a href="@addfeed">new feeds may be added</a>. For each feed or feed category, the <em>latest items</em> block may be enabled at the <a href="@block">blocks administration page</a>.', array('@addfeed' => url('admin/config/services/aggregator/add/feed'), '@block' => url('admin/structure/block'))) . '</p>';
      return $output;
    case 'admin/config/services/aggregator/add/feed':
      return '<p>' . t('Add a feed in RSS, RDF or Atom format. A feed may only have one entry.') . '</p>';
    case 'admin/config/services/aggregator/add/category':
      return '<p>' . t('Categories allow feed items from different feeds to be grouped together. For example, several sport-related feeds may belong to a category named <em>Sports</em>. Feed items may be grouped automatically (by selecting a category when creating or editing a feed) or manually (via the <em>Categorize</em> page available from feed item listings). Each category provides its own feed page and block.') . '</p>';
    case 'admin/config/services/aggregator/add/opml':
      return '<p>' . t('<acronym title="Outline Processor Markup Language">OPML</acronym> is an XML format used to exchange multiple feeds between aggregators. A single OPML document may contain a collection of many feeds. Drupal can parse such a file and import all feeds at once, saving you the effort of adding them manually. You may either upload a local file from your computer or enter a URL where Drupal can download it.') . '</p>';
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
