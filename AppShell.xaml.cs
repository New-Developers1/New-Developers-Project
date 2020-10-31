using Talent.Views;
using Xamarin.Forms;

namespace Talent
{
    public partial class AppShell : Shell
    {
        public AppShell()
        {
            InitializeComponent();
            this.CurrentItem.CurrentItem = homePage;
            Routing.RegisterRoute(nameof(TargetPage), typeof(TargetPage));
            Routing.RegisterRoute(nameof(MessPage), typeof(MessPage));
            Routing.RegisterRoute(nameof(NewsPage), typeof(NewsPage));
            Routing.RegisterRoute(nameof(TestPage), typeof(TestPage));
            Routing.RegisterRoute(nameof(ProfilePage), typeof(ProfilePage));
        }
    }
}
