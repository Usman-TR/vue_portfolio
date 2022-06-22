<template>
  <div id="nav">
    <router-link to="/">
        <svg class="nav_icon nav_icon_main" width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12.25 8.25C12.25 7.45435 12.5661 6.69129 13.1287 6.12868C13.6913 5.56607 14.4544 5.25 15.25 5.25H21.25C21.4489 5.25 21.6397 5.32902 21.7803 5.46967C21.921 5.61032 22 5.80109 22 6V18C22 18.1989 21.921 18.3897 21.7803 18.5303C21.6397 18.671 21.4489 18.75 21.25 18.75H15.25C14.4544 18.75 13.6913 19.0661 13.1287 19.6287C12.5661 20.1913 12.25 20.9544 12.25 21.75" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M2.5 18C2.5 18.1989 2.57902 18.3897 2.71967 18.5303C2.86032 18.671 3.05109 18.75 3.25 18.75H9.25C10.0456 18.75 10.8087 19.0661 11.3713 19.6287C11.9339 20.1913 12.25 20.9544 12.25 21.75V8.25C12.25 7.45435 11.9339 6.69129 11.3713 6.12868C10.8087 5.56607 10.0456 5.25 9.25 5.25H3.25C3.05109 5.25 2.86032 5.32902 2.71967 5.46967C2.57902 5.61032 2.5 5.80109 2.5 6V18Z" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span class="nav_btn_label">Главная</span>
    </router-link>

    <router-link v-if="this.$store.state.user.expert" to="/expert">
        <svg class="nav_icon nav_icon_expert" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20.2507 6.75H3.75073C3.33652 6.75 3.00073 7.08579 3.00073 7.5V19.5C3.00073 19.9142 3.33652 20.25 3.75073 20.25H20.2507C20.6649 20.25 21.0007 19.9142 21.0007 19.5V7.5C21.0007 7.08579 20.6649 6.75 20.2507 6.75Z" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M15.75 6.75V5.25C15.75 4.85218 15.592 4.47064 15.3107 4.18934C15.0294 3.90804 14.6478 3.75 14.25 3.75H9.75C9.35218 3.75 8.97064 3.90804 8.68934 4.18934C8.40804 4.47064 8.25 4.85218 8.25 5.25V6.75" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M21.0008 11.8414C18.2654 13.424 15.1602 14.2549 12 14.2499C8.84038 14.2549 5.73564 13.4243 3.00061 11.8422" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M10.875 11.25H13.125" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span class="nav_btn_label">Заявки</span>
    </router-link>

    <router-link v-if="this.$store.state.user.authentificated" to="/profile">
        <svg width="24" height="24" class="nav_icon nav_icon_profile" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 15.375C14.2782 15.375 16.125 13.5282 16.125 11.25C16.125 8.97183 14.2782 7.125 12 7.125C9.72183 7.125 7.875 8.97183 7.875 11.25C7.875 13.5282 9.72183 15.375 12 15.375Z" fill="black"/>
            <path d="M12 2.25C10.0716 2.25 8.18657 2.82183 6.58319 3.89317C4.97982 4.96452 3.73013 6.48726 2.99218 8.26884C2.25422 10.0504 2.06114 12.0108 2.43735 13.9021C2.81355 15.7934 3.74215 17.5307 5.10571 18.8943C6.46928 20.2579 8.20656 21.1865 10.0979 21.5627C11.9892 21.9389 13.9496 21.7458 15.7312 21.0078C17.5127 20.2699 19.0355 19.0202 20.1068 17.4168C21.1782 15.8134 21.75 13.9284 21.75 12C21.7471 9.41504 20.7189 6.93679 18.8911 5.10894C17.0632 3.28109 14.585 2.25293 12 2.25V2.25ZM18.1648 17.476C17.5628 16.6037 16.782 15.8695 15.8744 15.3221C14.8308 16.3188 13.4432 16.875 12 16.875C10.5569 16.875 9.16923 16.3188 8.12558 15.3221C7.218 15.8695 6.43724 16.6037 5.83516 17.476C4.77814 16.2874 4.08725 14.8186 3.84568 13.2464C3.60411 11.6743 3.82217 10.0658 4.4736 8.6147C5.12502 7.16361 6.18204 5.93177 7.51737 5.06752C8.85269 4.20327 10.4094 3.74346 12 3.74346C13.5906 3.74346 15.1473 4.20327 16.4826 5.06752C17.8179 5.93177 18.875 7.16361 19.5264 8.6147C20.1778 10.0658 20.3959 11.6743 20.1543 13.2464C19.9127 14.8186 19.2218 16.2874 18.1648 17.476V17.476Z" fill="black"/>
        </svg>

        <span class="nav_btn_label">Профиль</span>
    </router-link>
    <router-link v-else to="/login">
        <svg class="nav_icon nav_icon_login" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 15.375C14.2782 15.375 16.125 13.5282 16.125 11.25C16.125 8.97183 14.2782 7.125 12 7.125C9.72183 7.125 7.875 8.97183 7.875 11.25C7.875 13.5282 9.72183 15.375 12 15.375Z" fill="black"/>
            <path d="M12 2.25C10.0716 2.25 8.18657 2.82183 6.58319 3.89317C4.97982 4.96452 3.73013 6.48726 2.99218 8.26884C2.25422 10.0504 2.06114 12.0108 2.43735 13.9021C2.81355 15.7934 3.74215 17.5307 5.10571 18.8943C6.46928 20.2579 8.20656 21.1865 10.0979 21.5627C11.9892 21.9389 13.9496 21.7458 15.7312 21.0078C17.5127 20.2699 19.0355 19.0202 20.1068 17.4168C21.1782 15.8134 21.75 13.9284 21.75 12C21.7471 9.41504 20.7189 6.93679 18.8911 5.10894C17.0632 3.28109 14.585 2.25293 12 2.25V2.25ZM18.1648 17.476C17.5628 16.6037 16.782 15.8695 15.8744 15.3221C14.8308 16.3188 13.4432 16.875 12 16.875C10.5569 16.875 9.16923 16.3188 8.12558 15.3221C7.218 15.8695 6.43724 16.6037 5.83516 17.476C4.77814 16.2874 4.08725 14.8186 3.84568 13.2464C3.60411 11.6743 3.82217 10.0658 4.4736 8.6147C5.12502 7.16361 6.18204 5.93177 7.51737 5.06752C8.85269 4.20327 10.4094 3.74346 12 3.74346C13.5906 3.74346 15.1473 4.20327 16.4826 5.06752C17.8179 5.93177 18.875 7.16361 19.5264 8.6147C20.1778 10.0658 20.3959 11.6743 20.1543 13.2464C19.9127 14.8186 19.2218 16.2874 18.1648 17.476V17.476Z" fill="black"/>
        </svg>
        <span class="nav_btn_label">Войти</span>
    </router-link>
    <!-- <div>{{this.$store.state}}</div> -->
  </div>
  <router-view/>
</template>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');

@media (min-width: 8px) {
  #app {
    font-family: 'Roboto', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    padding-bottom: 80px;
  }

  #nav {
    padding: 0px;
    position: fixed;
    z-index: 100;
    background-color: #fff;
    bottom: 0;
    left: 0;
    right: 0;
    height: 80px;
    display: flex;
    justify-content: space-around;

    a {
      display: flex;
      flex-flow: column nowrap;
      align-items: center;
      justify-content: center;
      text-decoration: none
    }

    a {
      font-weight: bold;
      color: #2c3e50;

      &.router-link-exact-active {
        color: #835ED2;

        svg {
         fill: #000;
        //  filter: invert(0.5);
        }

        .nav_icon_profile {
          filter: invert(1);
          background: #fff;
          border-radius: 30px;
        }

      }
    }
  }
}
</style>
